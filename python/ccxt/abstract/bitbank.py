from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_pair_ticker = publicGetPairTicker = Entry('{pair}/ticker', 'public', 'GET', {})
    public_get_pair_depth = publicGetPairDepth = Entry('{pair}/depth', 'public', 'GET', {})
    public_get_pair_transactions = publicGetPairTransactions = Entry('{pair}/transactions', 'public', 'GET', {})
    public_get_pair_transactions_yyyymmdd = publicGetPairTransactionsYyyymmdd = Entry('{pair}/transactions/{yyyymmdd}', 'public', 'GET', {})
    public_get_pair_candlestick_candletype_yyyymmdd = publicGetPairCandlestickCandletypeYyyymmdd = Entry('{pair}/candlestick/{candletype}/{yyyymmdd}', 'public', 'GET', {})
    private_get_user_assets = privateGetUserAssets = Entry('user/assets', 'private', 'GET', {})
    private_get_user_spot_order = privateGetUserSpotOrder = Entry('user/spot/order', 'private', 'GET', {})
    private_get_user_spot_active_orders = privateGetUserSpotActiveOrders = Entry('user/spot/active_orders', 'private', 'GET', {})
    private_get_user_spot_trade_history = privateGetUserSpotTradeHistory = Entry('user/spot/trade_history', 'private', 'GET', {})
    private_get_user_withdrawal_account = privateGetUserWithdrawalAccount = Entry('user/withdrawal_account', 'private', 'GET', {})
    private_post_user_spot_order = privatePostUserSpotOrder = Entry('user/spot/order', 'private', 'POST', {})
    private_post_user_spot_cancel_order = privatePostUserSpotCancelOrder = Entry('user/spot/cancel_order', 'private', 'POST', {})
    private_post_user_spot_cancel_orders = privatePostUserSpotCancelOrders = Entry('user/spot/cancel_orders', 'private', 'POST', {})
    private_post_user_spot_orders_info = privatePostUserSpotOrdersInfo = Entry('user/spot/orders_info', 'private', 'POST', {})
    private_post_user_request_withdrawal = privatePostUserRequestWithdrawal = Entry('user/request_withdrawal', 'private', 'POST', {})
    markets_get_spot_pairs = marketsGetSpotPairs = Entry('spot/pairs', 'markets', 'GET', {})
