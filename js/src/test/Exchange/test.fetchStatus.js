// ----------------------------------------------------------------------------

// PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
// https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code
// EDIT THE CORRESPONDENT .ts FILE INSTEAD

// ----------------------------------------------------------------------------
import assert from 'assert';
// ----------------------------------------------------------------------------
export default async (exchange) => {
    const method = 'fetchStatus';
    if (exchange.has[method]) {
        const status = await exchange[method]();
        const sampleStatus = {
            'status': 'ok',
            'updated': undefined,
            'eta': undefined,
            'url': undefined, // a link to a GitHub issue or to an exchange post on the subject
        };
        const keys = Object.keys(sampleStatus);
        for (let i = 0; i < keys.length; i++) {
            const key = keys[i];
            assert(key in status);
        }
        return status;
    }
    else {
        console.log(method + '() is not supported');
    }
};
