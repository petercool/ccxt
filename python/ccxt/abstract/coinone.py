from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_orderbook = publicGetOrderbook = Entry('orderbook/', 'public', 'GET', {})
    public_get_trades = publicGetTrades = Entry('trades/', 'public', 'GET', {})
    public_get_ticker = publicGetTicker = Entry('ticker/', 'public', 'GET', {})
    private_post_account_deposit_address = privatePostAccountDepositAddress = Entry('account/deposit_address/', 'private', 'POST', {})
    private_post_account_btc_deposit_address = privatePostAccountBtcDepositAddress = Entry('account/btc_deposit_address/', 'private', 'POST', {})
    private_post_account_balance = privatePostAccountBalance = Entry('account/balance/', 'private', 'POST', {})
    private_post_account_daily_balance = privatePostAccountDailyBalance = Entry('account/daily_balance/', 'private', 'POST', {})
    private_post_account_user_info = privatePostAccountUserInfo = Entry('account/user_info/', 'private', 'POST', {})
    private_post_account_virtual_account = privatePostAccountVirtualAccount = Entry('account/virtual_account/', 'private', 'POST', {})
    private_post_order_cancel_all = privatePostOrderCancelAll = Entry('order/cancel_all/', 'private', 'POST', {})
    private_post_order_cancel = privatePostOrderCancel = Entry('order/cancel/', 'private', 'POST', {})
    private_post_order_limit_buy = privatePostOrderLimitBuy = Entry('order/limit_buy/', 'private', 'POST', {})
    private_post_order_limit_sell = privatePostOrderLimitSell = Entry('order/limit_sell/', 'private', 'POST', {})
    private_post_order_complete_orders = privatePostOrderCompleteOrders = Entry('order/complete_orders/', 'private', 'POST', {})
    private_post_order_limit_orders = privatePostOrderLimitOrders = Entry('order/limit_orders/', 'private', 'POST', {})
    private_post_order_order_info = privatePostOrderOrderInfo = Entry('order/order_info/', 'private', 'POST', {})
    private_post_transaction_auth_number = privatePostTransactionAuthNumber = Entry('transaction/auth_number/', 'private', 'POST', {})
    private_post_transaction_history = privatePostTransactionHistory = Entry('transaction/history/', 'private', 'POST', {})
    private_post_transaction_krw_history = privatePostTransactionKrwHistory = Entry('transaction/krw/history/', 'private', 'POST', {})
    private_post_transaction_btc = privatePostTransactionBtc = Entry('transaction/btc/', 'private', 'POST', {})
    private_post_transaction_coin = privatePostTransactionCoin = Entry('transaction/coin/', 'private', 'POST', {})
