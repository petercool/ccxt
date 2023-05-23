// -------------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

// -------------------------------------------------------------------------------

import { implicitReturnType } from '../base/types.js';
import { Exchange as _Exchange } from '../base/Exchange.js';

interface Exchange {
    exchangeGetMarkets (params?: {}): Promise<implicitReturnType>;
    publicGetOrderbook (params?: {}): Promise<implicitReturnType>;
    publicGetOrderbookTop (params?: {}): Promise<implicitReturnType>;
    publicGetTicker (params?: {}): Promise<implicitReturnType>;
    publicGetTickers (params?: {}): Promise<implicitReturnType>;
    publicGetTrades (params?: {}): Promise<implicitReturnType>;
    privateGetAccountsIdPending (params?: {}): Promise<implicitReturnType>;
    privateGetAccountsIdTransactions (params?: {}): Promise<implicitReturnType>;
    privateGetBalance (params?: {}): Promise<implicitReturnType>;
    privateGetBeneficiaries (params?: {}): Promise<implicitReturnType>;
    privateGetFeeInfo (params?: {}): Promise<implicitReturnType>;
    privateGetFundingAddress (params?: {}): Promise<implicitReturnType>;
    privateGetListorders (params?: {}): Promise<implicitReturnType>;
    privateGetListtrades (params?: {}): Promise<implicitReturnType>;
    privateGetOrdersId (params?: {}): Promise<implicitReturnType>;
    privateGetQuotesId (params?: {}): Promise<implicitReturnType>;
    privateGetWithdrawals (params?: {}): Promise<implicitReturnType>;
    privateGetWithdrawalsId (params?: {}): Promise<implicitReturnType>;
    privateGetTransfers (params?: {}): Promise<implicitReturnType>;
    privatePostAccounts (params?: {}): Promise<implicitReturnType>;
    privatePostAccountsIdName (params?: {}): Promise<implicitReturnType>;
    privatePostPostorder (params?: {}): Promise<implicitReturnType>;
    privatePostMarketorder (params?: {}): Promise<implicitReturnType>;
    privatePostStoporder (params?: {}): Promise<implicitReturnType>;
    privatePostFundingAddress (params?: {}): Promise<implicitReturnType>;
    privatePostWithdrawals (params?: {}): Promise<implicitReturnType>;
    privatePostSend (params?: {}): Promise<implicitReturnType>;
    privatePostQuotes (params?: {}): Promise<implicitReturnType>;
    privatePostOauth2Grant (params?: {}): Promise<implicitReturnType>;
    privatePutAccountsIdName (params?: {}): Promise<implicitReturnType>;
    privatePutQuotesId (params?: {}): Promise<implicitReturnType>;
    privateDeleteQuotesId (params?: {}): Promise<implicitReturnType>;
    privateDeleteWithdrawalsId (params?: {}): Promise<implicitReturnType>;
}
abstract class Exchange extends _Exchange {}

export default Exchange
