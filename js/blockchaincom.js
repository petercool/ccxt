'use strict';

//  ---------------------------------------------------------------------------
// Started Writing on Monday 27th September 2021
//  ---------------------------------------------------------------------------
const Exchange = require ('./base/Exchange');
const { ExchangeError, AuthenticationError, OrderNotFound, InsufficientFunds } = require ('./base/errors');
const { TICK_SIZE } = require ('./base/functions/number');
// const Precise = require ('./base/Precise');

// ---------------------------------------------------------------------------

module.exports = class blockchaincom extends Exchange {
    describe () {
        return this.deepExtend (super.describe (), {
            'id': 'blockchaincom',
            'secret': undefined,
            'name': 'blockchain.com',
            'countries': ['LX'],
            'rateLimit': 10000,
            'version': 'v3',
            'has': {
                'CORS': false,
                'fetchTrades': false,
                'fetchOHLCV': false,
                'fetchLedger': false,
                'fetchMarkets': true,
                'fetchMarket': true,
                'fetchTickers': true,
                'fetchTicker': true,
                'fetchOrderBook': true,
                'fetchL2OrderBook': true,
                'fetchL3OrderBook': true, // needs proper parsing
                'fetchOrder': true,
                'fetchOpenOrders': true,
                'fetchClosedOrders': true,
                'fetchPartiallyFilledOrders': true,
                'fetchCanceledOrders': true,
                'fetchExpiredOrders': true,
                'fetchRejectedOrders': true,
                'fetchBalance': true,
                'createOrder': true,
                'cancelOrder': true,
                'cancelOrders': true,
                'fetchWithdrawals': true,
                'fetchWithdrawal': true,
                'fetchDeposits': true,
                'fetchDeposit': true,
                'withdraw': true,
                'fetchTradingFees': true,
                'fetchWithdrawalWhitelist': true, // fetches exchange specific benficiary-ids needed for withdrawals
                'fetchMyTrades': true,
            },
            'timeframes': undefined,
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/99450025-3be60a00-2931-11eb-9302-f4fd8d8589aa.jpg',
                'test': {
                    'public': 'https://testnet-api.delta.exchange',
                    'private': 'https://testnet-api.delta.exchange',
                },
                'api': {
                    'public': 'https://api.blockchain.com/v3/exchange',
                    'private': 'https://api.blockchain.com/v3/exchange',
                },
                'www': 'https://blockchain.com',
                'doc': [
                    'https://api.blockchain.com/v3',
                ],
                'fees': 'https://exchange.blockchain.com/fees',
            },
            'api': {
                'public': {
                    'get': [
                        'tickers', // fetchTickers
                        'tickers/{symbol}', // fetchTicker
                        'symbols', // fetchMarkets
                        'symbols/{symbol}', // fetchMarket
                        'l2/{symbol}', // fetchL2OrderBook
                        'l3/{symbol}', // fetchL3OrderBook
                    ],
                },
                'private': {
                    'get': [
                        'fees', // fetchFees
                        'orders', // fetchOpenOrders, fetchClosedOrders
                        'orders/{orderId}', // fetchOrder(id)
                        'trades', // ** NULL
                        'fills', // fetchMyTrades
                        'deposits', // fetchDeposits
                        'deposits/{depositId}', // fetchDeposit
                        'accounts', // fetchBalance
                        'accounts/{account}/{currency}', // ** unused
                        'whitelist', // fetchWithdrawalWhitelist
                        'whitelist/{currency}', // fetchWithdrawalWhitelistByCurrency
                        'withdrawals', // fetchWithdrawalWhitelist
                        'withdrawals/{withdrawalId}', // fetchWithdrawalById
                    ],
                    'post': [
                        'orders', // createOrder
                        'deposits/{currency}', // fetchDepositAddress by currency (only crypto supported)
                        'withdrawals', // withdraw
                    ],
                    'delete': [
                        'orders', // cancelOrders
                        'orders/{orderId}', // cancelOrder
                    ],
                },
            },
            'fees': {
                'trading': {
                    'feeSide': 'get',
                    'tierBased': true,
                    'percentage': true,
                    'tiers': {
                        'taker': [
                            [0, 0.4 / 100],
                            [10000, 0.22 / 100],
                            [50000, 0.2 / 100],
                            [100000, 0.18 / 100],
                            [500000, 0.18 / 100],
                            [1000000, 0.18 / 100],
                            [2500000, 0.18 / 100],
                            [5000000, 0.16 / 100],
                            [25000000, 0.14 / 100],
                            [100000000, 0.11 / 100],
                            [500000000, 0.08 / 100],
                            [1000000000, 0.06 / 100],
                        ],
                        'maker': [
                            [0, 0.2 / 100],
                            [10000, 0.12 / 100],
                            [50000, 0.1 / 100],
                            [100000, 0.08 / 100],
                            [500000, 0.07 / 100],
                            [1000000, 0.06 / 100],
                            [2500000, 0.05 / 100],
                            [5000000, 0.04 / 100],
                            [25000000, 0.03 / 100],
                            [100000000, 0.02 / 100],
                            [500000000, 0.01 / 100],
                            [1000000000, 0],
                        ],
                    },
                },
            },
            'requiredCredentials': {
                'apiKey': false,
                'secret': true,
            },
            'precisionMode': TICK_SIZE,
            'exceptions': {
                'exact': {
                    '401': AuthenticationError,
                    '404': OrderNotFound,
                    // 500 insufficient funds
                    // 'errorCode' : unifiedErrorMethod, ... populate via testing
                },
                'broad': {
                    // help what is broad
                },
            },
        });
    }

    currencyId (code) {
        const currency = this.currency (code);
        const id = currency['id'];
        return id;
    }

    async fetchMarkets (params = {}) {
        // still needs fee information
        //
        // },
        // "USDC-GBP": {
        // "base_currency": "USDC",
        // "base_currency_scale": 6,
        // "counter_currency": "GBP",
        // "counter_currency_scale": 2,
        // "min_price_increment": 10000,
        // "min_price_increment_scale": 8,
        // "min_order_size": 500000000,
        // "min_order_size_scale": 8,
        // "max_order_size": 0,
        // "max_order_size_scale": 8,
        // "lot_size": 10000,
        // "lot_size_scale": 8,
        // "status": "open",
        // "id": 68,
        // "auction_price": 0,
        // "auction_size": 0,
        // "auction_time": "",
        // "imbalance": 0
        // }, ...
        //
        const markets = await this.publicGetSymbols (params);
        const marketIds = Object.keys (markets);
        const result = [];
        for (let i = 0; i < marketIds.length; i++) {
            const marketId = marketIds[i];
            const market = this.safeValue (markets, marketId);
            const baseId = this.safeString (market, 'base_currency');
            const quoteId = this.safeString (market, 'counter_currency');
            const base = this.safeCurrencyCode (baseId);
            const quote = this.safeCurrencyCode (quoteId);
            const numericId = this.safeNumber (market, 'id');
            let active = undefined;
            const marketState = this.safeString (market, 'status');
            if (marketState === 'open') {
                active = 'true';
            } else {
                active = 'false';
            }
            const minPriceIncrement = this.safeInteger (market, 'min_price_increment');
            const minPriceScale = this.safeInteger (market, 'min_price_increment_scale');
            const pricePrecision = minPriceIncrement * Math.pow (10, -minPriceScale);
            const lotSize = this.safeInteger (market, 'lot_size');
            const lotScale = this.safeInteger (market, 'lot_size_scale');
            const amountPrecision = lotSize * Math.pow (10, -lotScale);
            const precision = {
                'price': pricePrecision,
                'amount': amountPrecision,
            };
            const minOrderSize = this.safeInteger (market, 'min_order_size');
            const minOrderSizeScale = this.safeInteger (market, 'min_order_size_scale');
            const limits = {
                'amount': {
                    'min': minOrderSize * Math.pow (10, -minOrderSizeScale),
                    'max': undefined,
                },
                'price': {
                    'min': undefined,
                    'max': undefined,
                },
                'cost': {
                    'min': undefined,
                    'max': undefined,
                },
            };
            const symbol = base + '/' + quote;
            result.push ({
                'id': marketId,
                'numericId': numericId,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'precision': precision,
                'limits': limits,
                'active': active,
                'info': market,
            });
        }
        return result;
    }

    async fetchMarket (symbol, params = {}) {
        await this.loadMarkets ();
        return this.market (symbol);
    }

    async fetchOrderBook (symbol, limit = undefined, params = {}) {
        return await this.fetchL3OrderBook (symbol, limit, params);
    }

    async fetchL3OrderBook (symbol, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            'symbol': this.marketId (symbol),
        };
        if (limit !== undefined) {
            request['depth'] = limit;
        }
        const response = await this.publicGetL3Symbol (this.extend (request, params));
        return this.parseOrderBook (response, symbol, undefined, 'bids', 'asks', 'px', 'qty');
    }

    async fetchL2OrderBook (symbol, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            'symbol': this.marketId (symbol),
        };
        if (limit !== undefined) {
            request['depth'] = limit;
        }
        const response = await this.publicGetL2Symbol (this.extend (request, params));
        return this.parseOrderBook (response, symbol, undefined, 'bids', 'asks', 'px', 'qty');
    }

    parseTicker (ticker, market = undefined) {
        // {
        //   "symbol": "BTC-USD",
        //   "price_24h": 47791.86,
        //   "volume_24h": 362.88635738,
        //   "last_trade_price": 47587.75
        // }
        const marketId = this.safeString (ticker, 'symbol');
        const symbol = this.safeSymbol (marketId, market);
        const last = this.safeNumber (ticker, 'last_trade_price');
        const baseVolume = this.safeNumber (ticker, 'volume_24h');
        const open = this.safeNumber (ticker, 'price_24h');
        return this.safeTicker ({
            'symbol': symbol,
            'timestamp': undefined,
            'datetime': undefined,
            'high': undefined,
            'low': undefined,
            'bid': undefined,
            'bidVolume': undefined,
            'ask': undefined,
            'askVolume': undefined,
            'vwap': undefined,
            'open': open,
            'close': undefined,
            'last': last,
            'previousClose': undefined,
            'change': undefined,
            'percentage': undefined,
            'average': undefined,
            'baseVolume': baseVolume,
            'quoteVolume': undefined,
            'info': ticker,
        }, market);
    }

    async fetchTicker (symbol, params = {}) {
        await this.loadMarkets ();
        const market = this.market (symbol);
        const request = {
            'symbol': market['id'],
        };
        const response = await this.publicGetTickersSymbol (this.extend (request, params));
        return this.parseTicker (response, market);
    }

    async fetchTickers (symbols = undefined, params = {}) {
        await this.loadMarkets ();
        const tickers = await this.publicGetTickers (params);
        return this.parseTickers (tickers, symbols);
    }

    parseOrderState (state) {
        const states = {
            'OPEN': 'open',
            'REJECTED': 'rejected',
            'FILLED': 'closed',
            'CANCELED': 'canceled',
            'PART_FILLED': 'open',
            'EXPIRED': 'expired',
        };
        return this.safeString (states, state, state);
    }

    parseOrder (order, market = undefined) {
        // {
        // clOrdId: '00001',
        // ordType: 'MARKET',
        // ordStatus: 'FILLED',
        // side: 'BUY',
        // symbol: 'USDC-USDT',
        // exOrdId: '281775861306290',
        // price: null,
        // text: 'Fill',
        // lastShares: '30.0',
        // lastPx: '0.9999',
        // leavesQty: '0.0',
        // cumQty: '30.0',
        // avgPx: '0.9999',
        // timestamp: '1633940339619'
        // }
        //
        const clientOrderId = this.safeString (order, 'clOrdId');
        const type = this.safeStringLower (order, 'ordType');
        const statusId = this.safeString (order, 'ordStatus');
        const state = this.parseOrderState (statusId);
        const side = this.safeStringLower (order, 'side');
        const marketId = this.safeString (order, 'symbol');
        const symbol = this.safeSymbol (marketId, market);
        const exchangeOrderId = this.safeString (order, 'exOrdId');
        const price = (type !== 'market') ? this.safeString (order, 'price') : undefined;
        const filled = this.safeNumber (order, 'cumQty', undefined);
        const remaining = this.safeNumber (order, 'leavesQty', undefined);
        const average = this.safeNumber (order, 'avgPx', undefined);
        const timestamp = this.safeInteger (order, 'timestamp');
        const datetime = this.iso8601 (timestamp);
        const result = {
            'id': exchangeOrderId,
            'clientOrderId': clientOrderId,
            'datetime': datetime,
            'timestamp': timestamp,
            'lastTradeTimestamp': undefined,
            'status': state,
            'symbol': symbol,
            'type': type,
            'timeInForce': undefined,
            'side': side,
            'price': price,
            'average': average,
            'amount': filled + remaining, // 'ordered amount of base'
            'filled': filled,
            'remaining': remaining,
            'cost': undefined, // "'cost': 'filled' * 'price' (filling price used where available)"
            'trades': [], // "a list of order trades/executions"
            'fee': {},
            'info': order,
        };
        return result;
    }

    async createOrder (symbol, type, side, amount, price = undefined, params = {}) {
        const clientOrderId = this.safeString2 (params, 'clientOrderId', 'clOrdId', this.uuid16 ());
        await this.loadMarkets ();
        const market = this.market (symbol);
        const id = market['id'];
        const request = {
            // 'stopPx' : limit price
            // 'timeInForce' : "GTC" for Good Till Cancel, "IOC" for Immediate or Cancel, "FOK" for Fill or Kill, "GTD" Good Till Date
            // 'expireDate' : expiry date in the format YYYYMMDD
            // 'minQty' : The minimum quantity required for an IOC fill
            'symbol': id,
            'side': side.toUpperCase (),
            'orderQty': this.amountToPrecision (symbol, amount),
            'ordType': type.toUpperCase (), // LIMIT, MARKET, STOP, STOPLIMIT
            'clOrdId': clientOrderId,
        };
        params = this.omit (params, ['clientOrderId', 'clOrdId']);
        if (request['ordType'] === 'LIMIT') {
            request['price'] = this.priceToPrecision (symbol, price);
        }
        if (request['ordType'] === 'STOPLIMIT') {
            request['price'] = this.priceToPrecision (symbol, price);
            request['stopPx'] = this.priceToPrecision (symbol, price);
        }
        const response = await this.privatePostOrders (this.extend (request, params));
        return this.parseOrder (response, market);
    }

    async cancelOrder (id, symbol = undefined, params = {}) {
        const request = {
            'orderId': id,
        };
        const response = await this.privateDeleteOrdersOrderId (this.extend (request, params));
        return {
            'id': id,
            'info': response,
        };
    }

    async cancelOrders (ids, symbol = undefined, params = {}) {
        // cancels all open orders if no symbol specified
        // cancels all open orders of given symbol, if symbol is specified
        await this.loadMarkets ();
        const request = {
            // 'symbol': marketId,
        };
        if (symbol !== undefined) {
            const marketId = this.marketId (symbol);
            request['symbol'] = marketId;
        }
        const response = await this.privateDeleteOrders (this.extend (request, params));
        return {
            'symbol': symbol,
            'info': response,
        };
    }

    async fetchTradingFees (params = {}) {
        //
        // {   makerRate: "0.002",
        // takerRate: "0.004",
        // volumeInUSD: "0.0"    }
        //
        await this.loadMarkets ();
        const response = await this.privateGetFees ();
        // no referance to funding fees in API
        return {
            'maker': this.safeNumber (response, 'makerRate'),
            'taker': this.safeNumber (response, 'takerRate'),
            'info': response,
        };
    }

    async fetchRejectedOrders (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        const state = 'REJECTED';
        return await this.fetchOrdersByState (state, symbol, since, limit, params);
    }

    async fetchCanceledOrders (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        const state = 'CANCELED';
        return await this.fetchOrdersByState (state, symbol, since, limit, params);
    }

    async fetchExpiredOrders (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        const state = 'EXPIRED';
        return await this.fetchOrdersByState (state, symbol, since, limit, params);
    }

    async fetchPartiallyFilledOrders (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        const state = 'PART_FILLED';
        return await this.fetchOrdersByState (state, symbol, since, limit, params);
    }

    async fetchClosedOrders (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        const state = 'FILLED';
        return await this.fetchOrdersByState (state, symbol, since, limit, params);
    }

    async fetchOpenOrders (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        const state = 'OPEN';
        return await this.fetchOrdersByState (state, symbol, since, limit, params);
    }

    async fetchOrdersByState (state, symbol = undefined, since = undefined, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            // 'to': unix epoch ms
            // 'from': unix epoch ms
            'status': state,
            'limit': 100,
        };
        let market = undefined;
        if (symbol !== undefined) {
            market = this.market (symbol);
            request['symbol'] = market['id'];
        }
        const response = await this.privateGetOrders (this.extend (request, params));
        return this.parseOrders (response, market, since, limit);
    }

    parseTrade (trade, market = undefined) {
        //
        // {"exOrdId":281685751028507,
        //   "tradeId":281685434947633,
        //   "execId":8847494003,
        //   "side":"BUY",
        //   "symbol":"AAVE-USDT",
        //   "price":405.34,
        //   "qty":0.1,
        //   "fee":0.162136,
        //   "timestamp":1634559249687}
        //
        const id = this.safeString (trade, 'exOrdId');
        const order = this.safeString (trade, 'tradeId');
        const side = this.safeString (trade, 'side').toLowerCase ();
        const marketId = this.safeString (trade, 'symbol');
        const symbol = this.safeSymbol (marketId, market);
        const price = this.safeNumber (trade, 'price');
        const amount = this.safeNumber (trade, 'qty');
        const timestamp = this.safeInteger (trade, 'timestamp');
        const datetime = this.iso8601 (timestamp);
        const feeCost = this.safeNumber (trade, 'fee');
        let feeCurrency = undefined;
        if (side === 'buy') {
            const base = symbol.split ('/')[0];
            feeCurrency = this.safeCurrencyCode (base);
        } else if (side === 'sell') {
            const quote = symbol.split ('/')[1];
            feeCurrency = this.safeCurrencyCode (quote);
        }
        const fee = { 'cost': feeCost, 'currency': feeCurrency };
        return {
            'id': id,
            'timestamp': timestamp,
            'datetime': datetime,
            'symbol': symbol,
            'order': order,
            'type': undefined,
            'side': side,
            'takerOrMaker': undefined,
            'price': price,
            'amount': amount,
            'cost': price * amount,
            'fee': fee,
            'info': order,
        };
    }

    async fetchMyTrades (symbol = undefined, since = undefined, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            'limit': limit ? limit : 100,
        };
        let market = undefined;
        if (symbol !== undefined) {
            request['symbol'] = this.marketId (symbol);
            market = this.market (symbol);
        }
        const trades = await this.privateGetFills (this.extend (request, params));
        return this.parseTrades (trades, market, since, limit, params); // need to define
    }

    async fetchDepositAddress (code, params = {}) {
        await this.loadMarkets ();
        const currency = this.currency (code);
        const request = {
            'currency': currency['id'],
        };
        const response = await this.privatePostDepositsCurrency (this.extend (request, params));
        const splitArr = this.safeString (response, 'address').split (':');
        const address = splitArr[0].trim ();
        const result = { 'info': response };
        result['currency'] = currency['code'];
        result['address'] = address;
        // if a tag or memo is used it is separated by a colon in the 'address' value
        if (splitArr[1] !== undefined) {
            const tag = splitArr[1].trim ();
            result['tag'] = tag;
        }
        return result;
    }

    parseTransactionState (state) {
        const states = {
            'COMPLETED': 'ok', //
            'REJECTED': 'failed',
            'PENDING': 'pending',
            'FAILED': 'failed',
            'REFUNDED': 'refunded',
        };
        return this.safeString (states, state, state);
    }

    parseTransaction (transaction, currency = undefined) {
        //
        // Deposit
        //  {
        //      "depositId":"748e9180-be0d-4a80-e175-0156150efc95",
        //      "amount":0.009,
        //      "currency":"ETH",
        //      "address":"0xEC6B5929D454C8D9546d4221ace969E1810Fa92c",
        //      "state":"COMPLETED",
        //      "txHash":"582114562140e51a80b481c2dfebaf62b4ab9769b8ff54820bb67e34d4a3ab0c",
        //      "timestamp":1633697196241},
        //
        // Withdrawal
        // { "amount":30.0,
        //   "currency":"USDT",
        //   "beneficiary":"cab00d11-6e7f-46b7-b453-2e8ef6f101fa", // blockchain specific id
        //   "withdrawalId":"99df5ef7-eab6-4033-be49-312930fbd1ea",
        //   "fee":34.005078,
        //   "state":"COMPLETED",
        //   "timestamp":1634218452549 }
        //
        let type = undefined;
        let id = undefined;
        const amount = this.safeNumber (transaction, 'amount');
        const timestamp = this.safeInteger (transaction, 'timestamp');
        const currencyId = this.safeString (transaction, 'currency');
        const code = this.safeCurrencyCode (currencyId, currency);
        const state = this.safeString (transaction, 'state');
        if ('depositId' in transaction) {
            type = 'deposit';
            id = this.safeString (transaction, 'depositId');
        } else if ('withdrawalId' in transaction) {
            type = 'withdrawal';
            id = this.safeString (transaction, 'withdrawalId');
        }
        const feeCost = (type === 'withdrawal') ? this.safeNumber (transaction, 'fee') : undefined;
        let fee = undefined;
        if (feeCost !== undefined) {
            fee = { 'currency': code, 'cost': feeCost };
        }
        const result = {
            'info': transaction,
            'id': id,
            'txid': (type === 'deposit') ? this.safeString (transaction, 'txhash') : undefined,
            'timestamp': timestamp,
            'datetime': this.iso8601 (timestamp),
            'addressFrom': undefined,
            'address': (type === 'deposit') ? this.safeString (transaction, 'address') : undefined,
            'addressTo': (type === 'deposit') ? this.safeString (transaction, 'address') : undefined,
            'tagFrom': undefined,
            'tag': undefined,
            'tagTo': undefined,
            'type': type,
            'amount': amount,
            'currency': code,
            'status': this.parseTransactionState (state), // 'status':   'pending',   // 'ok', 'failed', 'canceled', string
            'updated': undefined,
            'comment': undefined,
            'fee': fee,
        };
        return result;
    }

    async fetchWithdrawalWhitelist (params = {}) {
        await this.loadMarkets ();
        const response = await this.privateGetWhitelist ();
        const result = [];
        for (let i = 0; i < response.length; i++) {
            const entry = response[i];
            result.push ({
                'beneficiaryId': this.safeString (entry, 'whitelistId'),
                'name': this.safeString (entry, 'name'),
                'currency': this.safeString (entry, 'currency'),
                'info': entry,
            });
        }
        return result;
    }

    async fetchWithdrawalWhitelistByCurrency (currency, params = {}) {
        await this.loadMarkets ();
        const request = {
            'currency': this.currencyId (currency),
        };
        const response = await this.privateGetWhitelistCurrency (this.extend (request, params));
        const result = [];
        for (let i = 0; i < response.length; i++) {
            const entry = response[i];
            result.push ({
                'beneficiaryId': this.safeString (entry, 'whitelistId'),
                'name': this.safeString (entry, 'name'),
                'currency': this.safeString (entry, 'currency'),
                'info': entry,
            });
        }
        return result;
    }

    async withdraw (code, amount, address, tag = undefined, params = {}) {
        await this.loadMarkets ();
        const currencyid = this.currencyId (code);
        const request = {
            'amount': amount,
            'currency': currencyid,
            // 'beneficiary': address/id,
            'sendMax': false,
        };
        const response = await this.privatePostWithdrawals (this.extend (request, params));
        //
        // response:
        // {               amount: "30.0",
        //               currency: "USDT",
        //            beneficiary: "adcd43fb-9ba6-41f7-8c0d-7013482cb88f",
        //           withdrawalId: "99df5ef7-eab6-4033-be49-312930fbd1ea",
        //                    fee: "34.005078",
        //                  state: "PENDING",
        //              timestamp: "1634218452595"               },
        //
        const withdrawalId = this.safeString (response, 'withdrawalId');
        const result = {
            'info': response,
            'id': withdrawalId,
        };
        return result;
    }

    async fetchWithdrawals (code = undefined, since = undefined, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            // 'from' : integer timestamp in ms
            // 'to' : integer timestamp in ms
        };
        if (since !== undefined) {
            request['from'] = since;
        }
        const response = await this.privateGetWithdrawals (this.extend (request, params));
        return this.parseTransactions (response, code, since, limit);
    }

    async fetchWithdrawal (id, code = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            'withdrawalId': id,
        };
        const response = await this.privateGetWithdrawalsWithdrawalId (this.extend (request, params));
        return this.parseTransaction (response);
    }

    async fetchDeposits (code = undefined, since = undefined, limit = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            // 'from' : integer timestamp in ms
            // 'to' : integer timestap in ms
        };
        if (since !== undefined) {
            request['from'] = since;
        }
        const response = await this.privateGetDeposits (this.extend (request, params));
        return this.parseTransactions (response, code, since, limit);
    }

    async fetchDeposit (id, code = undefined, params = {}) {
        await this.loadMarkets ();
        const depositId = this.safeString (params, 'depositId', id);
        const request = {
            'depositId': depositId,
        };
        const deposit = await this.privateGetDepositsDepositId (this.extend (request, params));
        return this.parseTransaction (deposit);
    }

    async fetchBalance (params = {}) {
        await this.loadMarkets ();
        const accountName = this.safeString (params, 'account', 'primary');
        params = this.omit (params, 'account');
        const request = {
            'account': accountName,
        };
        const response = await this.privateGetAccounts (this.extend (request, params));
        // {"primary":
        //  [ {"currency":"ETH",
        //      "balance":0.009,
        //      "available":0.009,
        //      "balance_local":30.82869,
        //      "available_local":30.82869,
        //      "rate":3425.41}, ... ]
        //
        const balances = this.safeValue (response, accountName);
        if (balances === undefined) {
            throw new ExchangeError (this.id + ' fetchBalance() could not find the "' + accountName + '" account');
        }
        const result = { 'info': response };
        for (let i = 0; i < balances.length; i++) {
            const entry = balances[i];
            const currencyId = this.safeString (entry, 'currency');
            const code = this.safeCurrencyCode (currencyId);
            const account = this.account ();
            account['free'] = this.safeString (entry, 'available');
            account['total'] = this.safeString (entry, 'balance');
            result[code] = account;
        }
        return this.parseBalance (result);
    }

    async fetchOrder (id, symbol = undefined, params = {}) {
        await this.loadMarkets ();
        const request = {
            'orderId': id,
        };
        const response = await this.privateGetOrdersOrderId (this.extend (request, params));
        // fetch Order by Id
        // {
        // "exOrdId": 11111111,
        // "clOrdId": "ABC",
        // "ordType": "MARKET",
        // "ordStatus": "FILLED",
        // "side": "BUY",
        // "price": 0.12345,
        // "text": "string",
        // "symbol": "BTC-USD",
        // "lastShares": 0.5678,
        // "lastPx": 3500.12,
        // "leavesQty": 10,
        // "cumQty": 0.123345,
        // "avgPx": 345.33,
        // "timestamp": 1592830770594
        // }
        //
        return this.parseOrder (response);
    }

    sign (path, api = 'public', method = 'GET', params = {}, headers = undefined, body = undefined) {
        const requestPath = '/' + this.implodeParams (path, params);
        let url = this.urls['api'][api] + requestPath;
        const query = this.omit (params, this.extractParams (path));
        if (api === 'public') {
            if (Object.keys (query).length) {
                url += '?' + this.urlencode (query);
            }
        } else if (api === 'private') {
            this.checkRequiredCredentials ();
            headers = {
                'X-API-Token': this.secret,
            };
            if ((method === 'GET')) {
                if (Object.keys (query).length) {
                    url += '?' + this.urlencode (query);
                }
            } else {
                body = this.json (query);
                headers['Content-Type'] = 'application/json';
            }
        }
        return { 'url': url, 'method': method, 'body': body, 'headers': headers };
    }

    handleErrors (code, reason, url, method, headers, body, response, requestHeaders, requestBody) {
        // {"timestamp":"2021-10-21T15:13:58.837+00:00","status":404,"error":"Not Found","message":"","path":"/orders/505050"
        if (response === undefined) {
            return;
        }
        const text = this.safeString (response, 'text', undefined);
        if (text !== undefined) { // if trade currency account is empty returns 200 with rejected order
            if (text === 'Insufficient Balance') {
                throw new InsufficientFunds (this.id + ' ' + body);
            }
        }
        const errorCode = this.safeString (response, 'status');
        const errorMessage = this.safeString (response, 'error');
        if (code !== undefined) {
            const feedback = this.id + ' ' + this.json (response);
            this.throwExactlyMatchedException (this.exceptions['exact'], errorCode, feedback);
            this.throwBroadlyMatchedException (this.exceptions['broad'], errorMessage, feedback);
        }
    }
};
