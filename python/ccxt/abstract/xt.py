from ccxt.base.types import Entry


class ImplicitAPI:
    public_spot_get_currencies = publicSpotGetCurrencies = Entry('currencies', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_depth = publicSpotGetDepth = Entry('depth', ['public', 'spot'], 'GET', {'cost': 0.05})
    public_spot_get_kline = publicSpotGetKline = Entry('kline', ['public', 'spot'], 'GET', {'cost': 0.1})
    public_spot_get_symbol = publicSpotGetSymbol = Entry('symbol', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_ticker = publicSpotGetTicker = Entry('ticker', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_ticker_book = publicSpotGetTickerBook = Entry('ticker/book', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_ticker_price = publicSpotGetTickerPrice = Entry('ticker/price', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_ticker_24h = publicSpotGetTicker24h = Entry('ticker/24h', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_time = publicSpotGetTime = Entry('time', ['public', 'spot'], 'GET', {'cost': 1})
    public_spot_get_trade_history = publicSpotGetTradeHistory = Entry('trade/history', ['public', 'spot'], 'GET', {'cost': 0.1})
    public_spot_get_trade_recent = publicSpotGetTradeRecent = Entry('trade/recent', ['public', 'spot'], 'GET', {'cost': 0.1})
    public_spot_get_wallet_support_currency = publicSpotGetWalletSupportCurrency = Entry('wallet/support/currency', ['public', 'spot'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_contract_risk_balance = publicLinearGetFutureMarketV1PublicContractRiskBalance = Entry('future/market/v1/public/contract/risk-balance', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_contract_open_interest = publicLinearGetFutureMarketV1PublicContractOpenInterest = Entry('future/market/v1/public/contract/open-interest', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_leverage_bracket_detail = publicLinearGetFutureMarketV1PublicLeverageBracketDetail = Entry('future/market/v1/public/leverage/bracket/detail', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_leverage_bracket_list = publicLinearGetFutureMarketV1PublicLeverageBracketList = Entry('future/market/v1/public/leverage/bracket/list', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_agg_ticker = publicLinearGetFutureMarketV1PublicQAggTicker = Entry('future/market/v1/public/q/agg-ticker', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_agg_tickers = publicLinearGetFutureMarketV1PublicQAggTickers = Entry('future/market/v1/public/q/agg-tickers', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_deal = publicLinearGetFutureMarketV1PublicQDeal = Entry('future/market/v1/public/q/deal', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_depth = publicLinearGetFutureMarketV1PublicQDepth = Entry('future/market/v1/public/q/depth', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_funding_rate = publicLinearGetFutureMarketV1PublicQFundingRate = Entry('future/market/v1/public/q/funding-rate', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_funding_rate_record = publicLinearGetFutureMarketV1PublicQFundingRateRecord = Entry('future/market/v1/public/q/funding-rate-record', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_index_price = publicLinearGetFutureMarketV1PublicQIndexPrice = Entry('future/market/v1/public/q/index-price', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_kline = publicLinearGetFutureMarketV1PublicQKline = Entry('future/market/v1/public/q/kline', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_mark_price = publicLinearGetFutureMarketV1PublicQMarkPrice = Entry('future/market/v1/public/q/mark-price', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_symbol_index_price = publicLinearGetFutureMarketV1PublicQSymbolIndexPrice = Entry('future/market/v1/public/q/symbol-index-price', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_symbol_mark_price = publicLinearGetFutureMarketV1PublicQSymbolMarkPrice = Entry('future/market/v1/public/q/symbol-mark-price', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_ticker = publicLinearGetFutureMarketV1PublicQTicker = Entry('future/market/v1/public/q/ticker', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_q_tickers = publicLinearGetFutureMarketV1PublicQTickers = Entry('future/market/v1/public/q/tickers', ['public', 'linear'], 'GET', {'cost': 1})
    public_linear_get_future_market_v1_public_symbol_coins = publicLinearGetFutureMarketV1PublicSymbolCoins = Entry('future/market/v1/public/symbol/coins', ['public', 'linear'], 'GET', {'cost': 3.33})
    public_linear_get_future_market_v1_public_symbol_detail = publicLinearGetFutureMarketV1PublicSymbolDetail = Entry('future/market/v1/public/symbol/detail', ['public', 'linear'], 'GET', {'cost': 3.33})
    public_linear_get_future_market_v1_public_symbol_list = publicLinearGetFutureMarketV1PublicSymbolList = Entry('future/market/v1/public/symbol/list', ['public', 'linear'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_contract_risk_balance = publicInverseGetFutureMarketV1PublicContractRiskBalance = Entry('future/market/v1/public/contract/risk-balance', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_contract_open_interest = publicInverseGetFutureMarketV1PublicContractOpenInterest = Entry('future/market/v1/public/contract/open-interest', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_leverage_bracket_detail = publicInverseGetFutureMarketV1PublicLeverageBracketDetail = Entry('future/market/v1/public/leverage/bracket/detail', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_leverage_bracket_list = publicInverseGetFutureMarketV1PublicLeverageBracketList = Entry('future/market/v1/public/leverage/bracket/list', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_agg_ticker = publicInverseGetFutureMarketV1PublicQAggTicker = Entry('future/market/v1/public/q/agg-ticker', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_agg_tickers = publicInverseGetFutureMarketV1PublicQAggTickers = Entry('future/market/v1/public/q/agg-tickers', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_deal = publicInverseGetFutureMarketV1PublicQDeal = Entry('future/market/v1/public/q/deal', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_depth = publicInverseGetFutureMarketV1PublicQDepth = Entry('future/market/v1/public/q/depth', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_funding_rate = publicInverseGetFutureMarketV1PublicQFundingRate = Entry('future/market/v1/public/q/funding-rate', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_funding_rate_record = publicInverseGetFutureMarketV1PublicQFundingRateRecord = Entry('future/market/v1/public/q/funding-rate-record', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_index_price = publicInverseGetFutureMarketV1PublicQIndexPrice = Entry('future/market/v1/public/q/index-price', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_kline = publicInverseGetFutureMarketV1PublicQKline = Entry('future/market/v1/public/q/kline', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_mark_price = publicInverseGetFutureMarketV1PublicQMarkPrice = Entry('future/market/v1/public/q/mark-price', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_symbol_index_price = publicInverseGetFutureMarketV1PublicQSymbolIndexPrice = Entry('future/market/v1/public/q/symbol-index-price', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_symbol_mark_price = publicInverseGetFutureMarketV1PublicQSymbolMarkPrice = Entry('future/market/v1/public/q/symbol-mark-price', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_ticker = publicInverseGetFutureMarketV1PublicQTicker = Entry('future/market/v1/public/q/ticker', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_q_tickers = publicInverseGetFutureMarketV1PublicQTickers = Entry('future/market/v1/public/q/tickers', ['public', 'inverse'], 'GET', {'cost': 1})
    public_inverse_get_future_market_v1_public_symbol_coins = publicInverseGetFutureMarketV1PublicSymbolCoins = Entry('future/market/v1/public/symbol/coins', ['public', 'inverse'], 'GET', {'cost': 3.33})
    public_inverse_get_future_market_v1_public_symbol_detail = publicInverseGetFutureMarketV1PublicSymbolDetail = Entry('future/market/v1/public/symbol/detail', ['public', 'inverse'], 'GET', {'cost': 3.33})
    public_inverse_get_future_market_v1_public_symbol_list = publicInverseGetFutureMarketV1PublicSymbolList = Entry('future/market/v1/public/symbol/list', ['public', 'inverse'], 'GET', {'cost': 1})
    private_spot_get_balance = privateSpotGetBalance = Entry('balance', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_balances = privateSpotGetBalances = Entry('balances', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_batch_order = privateSpotGetBatchOrder = Entry('batch-order', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_deposit_address = privateSpotGetDepositAddress = Entry('deposit/address', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_deposit_history = privateSpotGetDepositHistory = Entry('deposit/history', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_history_order = privateSpotGetHistoryOrder = Entry('history-order', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_open_order = privateSpotGetOpenOrder = Entry('open-order', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_order = privateSpotGetOrder = Entry('order', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_order_orderid = privateSpotGetOrderOrderId = Entry('order/{orderId}', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_trade = privateSpotGetTrade = Entry('trade', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_get_withdraw_history = privateSpotGetWithdrawHistory = Entry('withdraw/history', ['private', 'spot'], 'GET', {'cost': 1})
    private_spot_post_order = privateSpotPostOrder = Entry('order', ['private', 'spot'], 'POST', {'cost': 0.2})
    private_spot_post_withdraw = privateSpotPostWithdraw = Entry('withdraw', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_balance_transfer = privateSpotPostBalanceTransfer = Entry('balance/transfer', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_post_balance_account_transfer = privateSpotPostBalanceAccountTransfer = Entry('balance/account/transfer', ['private', 'spot'], 'POST', {'cost': 1})
    private_spot_delete_batch_order = privateSpotDeleteBatchOrder = Entry('batch-order', ['private', 'spot'], 'DELETE', {'cost': 1})
    private_spot_delete_open_order = privateSpotDeleteOpenOrder = Entry('open-order', ['private', 'spot'], 'DELETE', {'cost': 1})
    private_spot_delete_order_orderid = privateSpotDeleteOrderOrderId = Entry('order/{orderId}', ['private', 'spot'], 'DELETE', {'cost': 1})
    private_linear_get_future_trade_v1_entrust_plan_detail = privateLinearGetFutureTradeV1EntrustPlanDetail = Entry('future/trade/v1/entrust/plan-detail', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_entrust_plan_list = privateLinearGetFutureTradeV1EntrustPlanList = Entry('future/trade/v1/entrust/plan-list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_entrust_plan_list_history = privateLinearGetFutureTradeV1EntrustPlanListHistory = Entry('future/trade/v1/entrust/plan-list-history', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_entrust_profit_detail = privateLinearGetFutureTradeV1EntrustProfitDetail = Entry('future/trade/v1/entrust/profit-detail', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_entrust_profit_list = privateLinearGetFutureTradeV1EntrustProfitList = Entry('future/trade/v1/entrust/profit-list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_order_detail = privateLinearGetFutureTradeV1OrderDetail = Entry('future/trade/v1/order/detail', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_order_list = privateLinearGetFutureTradeV1OrderList = Entry('future/trade/v1/order/list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_order_list_history = privateLinearGetFutureTradeV1OrderListHistory = Entry('future/trade/v1/order/list-history', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_trade_v1_order_trade_list = privateLinearGetFutureTradeV1OrderTradeList = Entry('future/trade/v1/order/trade-list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_account_info = privateLinearGetFutureUserV1AccountInfo = Entry('future/user/v1/account/info', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_balance_bills = privateLinearGetFutureUserV1BalanceBills = Entry('future/user/v1/balance/bills', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_balance_detail = privateLinearGetFutureUserV1BalanceDetail = Entry('future/user/v1/balance/detail', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_balance_funding_rate_list = privateLinearGetFutureUserV1BalanceFundingRateList = Entry('future/user/v1/balance/funding-rate-list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_balance_list = privateLinearGetFutureUserV1BalanceList = Entry('future/user/v1/balance/list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_position_adl = privateLinearGetFutureUserV1PositionAdl = Entry('future/user/v1/position/adl', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_position_list = privateLinearGetFutureUserV1PositionList = Entry('future/user/v1/position/list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_user_collection_list = privateLinearGetFutureUserV1UserCollectionList = Entry('future/user/v1/user/collection/list', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_get_future_user_v1_user_listen_key = privateLinearGetFutureUserV1UserListenKey = Entry('future/user/v1/user/listen-key', ['private', 'linear'], 'GET', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_cancel_all_plan = privateLinearPostFutureTradeV1EntrustCancelAllPlan = Entry('future/trade/v1/entrust/cancel-all-plan', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_cancel_all_profit_stop = privateLinearPostFutureTradeV1EntrustCancelAllProfitStop = Entry('future/trade/v1/entrust/cancel-all-profit-stop', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_cancel_plan = privateLinearPostFutureTradeV1EntrustCancelPlan = Entry('future/trade/v1/entrust/cancel-plan', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_cancel_profit_stop = privateLinearPostFutureTradeV1EntrustCancelProfitStop = Entry('future/trade/v1/entrust/cancel-profit-stop', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_create_plan = privateLinearPostFutureTradeV1EntrustCreatePlan = Entry('future/trade/v1/entrust/create-plan', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_create_profit = privateLinearPostFutureTradeV1EntrustCreateProfit = Entry('future/trade/v1/entrust/create-profit', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_entrust_update_profit_stop = privateLinearPostFutureTradeV1EntrustUpdateProfitStop = Entry('future/trade/v1/entrust/update-profit-stop', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_order_cancel = privateLinearPostFutureTradeV1OrderCancel = Entry('future/trade/v1/order/cancel', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_order_cancel_all = privateLinearPostFutureTradeV1OrderCancelAll = Entry('future/trade/v1/order/cancel-all', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_order_create = privateLinearPostFutureTradeV1OrderCreate = Entry('future/trade/v1/order/create', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_trade_v1_order_create_batch = privateLinearPostFutureTradeV1OrderCreateBatch = Entry('future/trade/v1/order/create-batch', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_account_open = privateLinearPostFutureUserV1AccountOpen = Entry('future/user/v1/account/open', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_position_adjust_leverage = privateLinearPostFutureUserV1PositionAdjustLeverage = Entry('future/user/v1/position/adjust-leverage', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_position_auto_margin = privateLinearPostFutureUserV1PositionAutoMargin = Entry('future/user/v1/position/auto-margin', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_position_close_all = privateLinearPostFutureUserV1PositionCloseAll = Entry('future/user/v1/position/close-all', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_position_margin = privateLinearPostFutureUserV1PositionMargin = Entry('future/user/v1/position/margin', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_user_collection_add = privateLinearPostFutureUserV1UserCollectionAdd = Entry('future/user/v1/user/collection/add', ['private', 'linear'], 'POST', {'cost': 1})
    private_linear_post_future_user_v1_user_collection_cancel = privateLinearPostFutureUserV1UserCollectionCancel = Entry('future/user/v1/user/collection/cancel', ['private', 'linear'], 'POST', {'cost': 1})
    private_inverse_get_future_trade_v1_entrust_plan_detail = privateInverseGetFutureTradeV1EntrustPlanDetail = Entry('future/trade/v1/entrust/plan-detail', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_entrust_plan_list = privateInverseGetFutureTradeV1EntrustPlanList = Entry('future/trade/v1/entrust/plan-list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_entrust_plan_list_history = privateInverseGetFutureTradeV1EntrustPlanListHistory = Entry('future/trade/v1/entrust/plan-list-history', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_entrust_profit_detail = privateInverseGetFutureTradeV1EntrustProfitDetail = Entry('future/trade/v1/entrust/profit-detail', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_entrust_profit_list = privateInverseGetFutureTradeV1EntrustProfitList = Entry('future/trade/v1/entrust/profit-list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_order_detail = privateInverseGetFutureTradeV1OrderDetail = Entry('future/trade/v1/order/detail', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_order_list = privateInverseGetFutureTradeV1OrderList = Entry('future/trade/v1/order/list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_order_list_history = privateInverseGetFutureTradeV1OrderListHistory = Entry('future/trade/v1/order/list-history', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_trade_v1_order_trade_list = privateInverseGetFutureTradeV1OrderTradeList = Entry('future/trade/v1/order/trade-list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_account_info = privateInverseGetFutureUserV1AccountInfo = Entry('future/user/v1/account/info', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_balance_bills = privateInverseGetFutureUserV1BalanceBills = Entry('future/user/v1/balance/bills', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_balance_detail = privateInverseGetFutureUserV1BalanceDetail = Entry('future/user/v1/balance/detail', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_balance_funding_rate_list = privateInverseGetFutureUserV1BalanceFundingRateList = Entry('future/user/v1/balance/funding-rate-list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_balance_list = privateInverseGetFutureUserV1BalanceList = Entry('future/user/v1/balance/list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_position_adl = privateInverseGetFutureUserV1PositionAdl = Entry('future/user/v1/position/adl', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_position_list = privateInverseGetFutureUserV1PositionList = Entry('future/user/v1/position/list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_user_collection_list = privateInverseGetFutureUserV1UserCollectionList = Entry('future/user/v1/user/collection/list', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_get_future_user_v1_user_listen_key = privateInverseGetFutureUserV1UserListenKey = Entry('future/user/v1/user/listen-key', ['private', 'inverse'], 'GET', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_cancel_all_plan = privateInversePostFutureTradeV1EntrustCancelAllPlan = Entry('future/trade/v1/entrust/cancel-all-plan', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_cancel_all_profit_stop = privateInversePostFutureTradeV1EntrustCancelAllProfitStop = Entry('future/trade/v1/entrust/cancel-all-profit-stop', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_cancel_plan = privateInversePostFutureTradeV1EntrustCancelPlan = Entry('future/trade/v1/entrust/cancel-plan', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_cancel_profit_stop = privateInversePostFutureTradeV1EntrustCancelProfitStop = Entry('future/trade/v1/entrust/cancel-profit-stop', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_create_plan = privateInversePostFutureTradeV1EntrustCreatePlan = Entry('future/trade/v1/entrust/create-plan', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_create_profit = privateInversePostFutureTradeV1EntrustCreateProfit = Entry('future/trade/v1/entrust/create-profit', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_entrust_update_profit_stop = privateInversePostFutureTradeV1EntrustUpdateProfitStop = Entry('future/trade/v1/entrust/update-profit-stop', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_order_cancel = privateInversePostFutureTradeV1OrderCancel = Entry('future/trade/v1/order/cancel', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_order_cancel_all = privateInversePostFutureTradeV1OrderCancelAll = Entry('future/trade/v1/order/cancel-all', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_order_create = privateInversePostFutureTradeV1OrderCreate = Entry('future/trade/v1/order/create', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_trade_v1_order_create_batch = privateInversePostFutureTradeV1OrderCreateBatch = Entry('future/trade/v1/order/create-batch', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_account_open = privateInversePostFutureUserV1AccountOpen = Entry('future/user/v1/account/open', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_position_adjust_leverage = privateInversePostFutureUserV1PositionAdjustLeverage = Entry('future/user/v1/position/adjust-leverage', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_position_auto_margin = privateInversePostFutureUserV1PositionAutoMargin = Entry('future/user/v1/position/auto-margin', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_position_close_all = privateInversePostFutureUserV1PositionCloseAll = Entry('future/user/v1/position/close-all', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_position_margin = privateInversePostFutureUserV1PositionMargin = Entry('future/user/v1/position/margin', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_user_collection_add = privateInversePostFutureUserV1UserCollectionAdd = Entry('future/user/v1/user/collection/add', ['private', 'inverse'], 'POST', {'cost': 1})
    private_inverse_post_future_user_v1_user_collection_cancel = privateInversePostFutureUserV1UserCollectionCancel = Entry('future/user/v1/user/collection/cancel', ['private', 'inverse'], 'POST', {'cost': 1})
    private_user_get_user_account = privateUserGetUserAccount = Entry('user/account', ['private', 'user'], 'GET', {'cost': 1})
    private_user_get_user_account_api_key = privateUserGetUserAccountApiKey = Entry('user/account/api-key', ['private', 'user'], 'GET', {'cost': 1})
    private_user_post_user_account = privateUserPostUserAccount = Entry('user/account', ['private', 'user'], 'POST', {'cost': 1})
    private_user_post_user_account_api_key = privateUserPostUserAccountApiKey = Entry('user/account/api-key', ['private', 'user'], 'POST', {'cost': 1})
    private_user_put_user_account_api_key = privateUserPutUserAccountApiKey = Entry('user/account/api-key', ['private', 'user'], 'PUT', {'cost': 1})
    private_user_delete_user_account_apikeyid = privateUserDeleteUserAccountApikeyId = Entry('user/account/{apikeyId}', ['private', 'user'], 'DELETE', {'cost': 1})
