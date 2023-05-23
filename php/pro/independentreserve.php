<?php

namespace ccxt\pro;

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

use Exception; // a common import
use ccxt\NotSupported;
use ccxt\InvalidNonce;
use React\Async;

class independentreserve extends \ccxt\async\independentreserve {

    public function describe() {
        return $this->deep_extend(parent::describe(), array(
            'has' => array(
                'ws' => true,
                'watchBalance' => false,
                'watchTicker' => false,
                'watchTickers' => false,
                'watchTrades' => true,
                'watchMyTrades' => false,
                'watchOrders' => false,
                'watchOrderBook' => true,
                'watchOHLCV' => false,
            ),
            'urls' => array(
                'api' => array(
                    'ws' => 'wss://websockets.independentreserve.com',
                ),
            ),
            'options' => array(
                'checksum' => false, // TODO => currently only working for snapshot
            ),
            'streaming' => array(
            ),
            'exceptions' => array(
            ),
        ));
    }

    public function watch_trades(string $symbol, ?int $since = null, ?int $limit = null, $params = array ()) {
        return Async\async(function () use ($symbol, $since, $limit, $params) {
            /**
             * get the list of most recent $trades for a particular $symbol
             * @param {string} $symbol unified $symbol of the $market to fetch $trades for
             * @param {int|null} $since timestamp in ms of the earliest trade to fetch
             * @param {int|null} $limit the maximum amount of $trades to fetch
             * @param {array} $params extra parameters specific to the independentreserve api endpoint
             * @return {[array]} a list of ~@link https://docs.ccxt.com/en/latest/manual.html?#public-$trades trade structures~
             */
            Async\await($this->load_markets());
            $market = $this->market($symbol);
            $symbol = $market['symbol'];
            $url = $this->urls['api']['ws'] . '?subscribe=ticker-' . $market['base'] . '-' . $market['quote'];
            $messageHash = 'trades:' . $symbol;
            $trades = Async\await($this->watch($url, $messageHash, null, $messageHash));
            return $this->filter_by_since_limit($trades, $since, $limit, 'timestamp');
        }) ();
    }

    public function handle_trades(Client $client, $message) {
        //
        //    {
        //        Channel => 'ticker-btc-usd',
        //        Nonce => 130,
        //        Data => array(
        //          TradeGuid => '7a669f2a-d564-472b-8493-6ef982eb1e96',
        //          Pair => 'btc-aud',
        //          TradeDate => '2023-02-12T10:04:13.0804889+11:00',
        //          Price => 31640,
        //          Volume => 0.00079029,
        //          BidGuid => 'ba8a78b5-be69-4d33-92bb-9df0daa6314e',
        //          OfferGuid => '27d20270-f21f-4c25-9905-152e70b2f6ec',
        //          Side => 'Buy'
        //        ),
        //        Time => 1676156653111,
        //        Event => 'Trade'
        //    }
        //
        $data = $this->safe_value($message, 'Data', array());
        $marketId = $this->safe_string($data, 'Pair');
        $symbol = $this->safe_symbol($marketId, null, '-');
        $messageHash = 'trades:' . $symbol;
        $stored = $this->safe_value($this->trades, $symbol);
        if ($stored === null) {
            $limit = $this->safe_integer($this->options, 'tradesLimit', 1000);
            $stored = new ArrayCache ($limit);
            $this->trades[$symbol] = $stored;
        }
        $trade = $this->parse_ws_trade($data);
        $stored->append ($trade);
        $this->trades[$symbol] = $stored;
        $client->resolve ($this->trades[$symbol], $messageHash);
    }

    public function parse_ws_trade($trade, $market = null) {
        //
        //    {
        //        "TradeGuid" => "2f316718-0d0b-4e33-a30c-c2c06f3cfb34",
        //        "Pair" => "xbt-aud",
        //        "TradeDate" => "2023-02-12T09:22:35.4207494+11:00",
        //        "Price" => 31573.8,
        //        "Volume" => 0.05,
        //        "BidGuid" => "adb63d74-4c02-47f9-9cc3-f287e3b48ab6",
        //        "OfferGuid" => "b94d9bc4-addd-4633-a18f-69cf7e1b6f47",
        //        "Side" => "Buy"
        //    }
        //
        $datetime = $this->safe_string($trade, 'TradeDate');
        $marketId = $this->safe_string($market, 'Pair');
        return $this->safe_trade(array(
            'info' => $trade,
            'id' => $this->safe_string($trade, 'TradeGuid'),
            'order' => $this->safe_string($trade, 'orderNo'),
            'symbol' => $this->safe_symbol($marketId, $market, '-'),
            'side' => $this->safe_string_lower($trade, 'Side'),
            'type' => null,
            'takerOrMaker' => null,
            'price' => $this->safe_string($trade, 'Price'),
            'amount' => $this->safe_string($trade, 'Volume'),
            'cost' => null,
            'fee' => null,
            'timestamp' => $this->parse8601($datetime),
            'datetime' => $datetime,
        ), $market);
    }

    public function watch_order_book(string $symbol, ?int $limit = null, $params = array ()) {
        return Async\async(function () use ($symbol, $limit, $params) {
            /**
             * watches information on open orders with bid (buy) and ask (sell) prices, volumes and other data
             * @param {string} $symbol unified $symbol of the $market to fetch the order book for
             * @param {int|null} $limit the maximum amount of order book entries to return
             * @param {array} $params extra parameters specific to the independentreserve api endpoint
             * @return {array} A dictionary of ~@link https://docs.ccxt.com/#/?id=order-book-structure order book structures~ indexed by $market symbols
             */
            Async\await($this->load_markets());
            $market = $this->market($symbol);
            $symbol = $market['symbol'];
            if ($limit === null) {
                $limit = 100;
            }
            $limit = $this->number_to_string($limit);
            $url = $this->urls['api']['ws'] . '/orderbook/' . $limit . '?subscribe=' . $market['base'] . '-' . $market['quote'];
            $messageHash = 'orderbook:' . $symbol . ':' . $limit;
            $subscription = array(
                'receivedSnapshot' => false,
            );
            $orderbook = Async\await($this->watch($url, $messageHash, null, $messageHash, $subscription));
            return $orderbook->limit ();
        }) ();
    }

    public function handle_order_book(Client $client, $message) {
        //
        //    {
        //        Channel => "orderbook/1/eth/aud",
        //        Data => array(
        //          Bids => array(
        //            array(
        //              Price => 2198.09,
        //              Volume => 0.16143952,
        //            ),
        //          ),
        //          Offers => array(
        //            array(
        //              Price => 2201.25,
        //              Volume => 15,
        //            ),
        //          ),
        //          Crc32 => 1519697650,
        //        ),
        //        Time => 1676150558254,
        //        Event => "OrderBookSnapshot",
        //    }
        //
        $event = $this->safe_string($message, 'Event');
        $channel = $this->safe_string($message, 'Channel');
        $parts = explode('/', $channel);
        $depth = $this->safe_string($parts, 1);
        $baseId = $this->safe_string($parts, 2);
        $quoteId = $this->safe_string($parts, 3);
        $base = $this->safe_currency_code($baseId);
        $quote = $this->safe_currency_code($quoteId);
        $symbol = $base . '/' . $quote;
        $orderBook = $this->safe_value($message, 'Data', array());
        $messageHash = 'orderbook:' . $symbol . ':' . $depth;
        $subscription = $this->safe_value($client->subscriptions, $messageHash, array());
        $receivedSnapshot = $this->safe_value($subscription, 'receivedSnapshot', false);
        $timestamp = $this->safe_integer($message, 'Time');
        $storedOrderBook = $this->safe_value($this->orderbooks, $symbol);
        if ($storedOrderBook === null) {
            $storedOrderBook = $this->order_book(array());
            $this->orderbooks[$symbol] = $storedOrderBook;
        }
        if ($event === 'OrderBookSnapshot') {
            $snapshot = $this->parse_order_book($orderBook, $symbol, $timestamp, 'Bids', 'Offers', 'Price', 'Volume');
            $storedOrderBook->reset ($snapshot);
            $subscription['receivedSnapshot'] = true;
        } else {
            $asks = $this->safe_value($orderBook, 'Offers', array());
            $bids = $this->safe_value($orderBook, 'Bids', array());
            $this->handle_deltas($storedOrderBook['asks'], $asks);
            $this->handle_deltas($storedOrderBook['bids'], $bids);
            $storedOrderBook['timestamp'] = $timestamp;
            $storedOrderBook['datetime'] = $this->iso8601($timestamp);
        }
        $checksum = $this->safe_value($this->options, 'checksum', true);
        if ($checksum && $receivedSnapshot) {
            $storedAsks = $storedOrderBook['asks'];
            $storedBids = $storedOrderBook['bids'];
            $asksLength = count($storedAsks);
            $bidsLength = count($storedBids);
            $payload = '';
            for ($i = 0; $i < 10; $i++) {
                if ($i < $bidsLength) {
                    $payload = $payload . $this->value_to_checksum($storedBids[$i][0]) . $this->value_to_checksum($storedBids[$i][1]);
                }
            }
            for ($i = 0; $i < 10; $i++) {
                if ($i < $asksLength) {
                    $payload = $payload . $this->value_to_checksum($storedAsks[$i][0]) . $this->value_to_checksum($storedAsks[$i][1]);
                }
            }
            $calculatedChecksum = $this->crc32($payload, true);
            $responseChecksum = $this->safe_integer($orderBook, 'Crc32');
            if ($calculatedChecksum !== $responseChecksum) {
                $error = new InvalidNonce ($this->id . ' invalid checksum');
                $client->reject ($error, $messageHash);
            }
        }
        if ($receivedSnapshot) {
            $client->resolve ($storedOrderBook, $messageHash);
        }
    }

    public function value_to_checksum($value) {
        $result = sprintf('%.8f', $value);
        $result = str_replace('.', '', $result);
        // remove leading zeros
        $result = $this->parse_number($result);
        $result = $this->number_to_string($result);
        return $result;
    }

    public function handle_delta($bookside, $delta) {
        $bidAsk = $this->parse_bid_ask($delta, 'Price', 'Volume');
        $bookside->storeArray ($bidAsk);
    }

    public function handle_deltas($bookside, $deltas) {
        for ($i = 0; $i < count($deltas); $i++) {
            $this->handle_delta($bookside, $deltas[$i]);
        }
    }

    public function handle_heartbeat(Client $client, $message) {
        //
        //    {
        //        Time => 1676156208182,
        //        Event => 'Heartbeat'
        //    }
        //
        return $message;
    }

    public function handle_subscriptions(Client $client, $message) {
        //
        //    {
        //        Data => array( 'ticker-btc-sgd' ),
        //        Time => 1676157556223,
        //        Event => 'Subscriptions'
        //    }
        //
        return $message;
    }

    public function handle_message(Client $client, $message) {
        $event = $this->safe_string($message, 'Event');
        $handlers = array(
            'Subscriptions' => array($this, 'handle_subscriptions'),
            'Heartbeat' => array($this, 'handle_heartbeat'),
            'Trade' => array($this, 'handle_trades'),
            'OrderBookSnapshot' => array($this, 'handle_order_book'),
            'OrderBookChange' => array($this, 'handle_order_book'),
        );
        $handler = $this->safe_value($handlers, $event);
        if ($handler !== null) {
            return $handler($client, $message);
        }
        throw new NotSupported($this->id . ' received an unsupported $message => ' . $this->json($message));
    }
}
