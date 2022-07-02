import hashlib

omipay_url = 'https://checkout-sandbox.omipay.vn/checkout.php'
secure_pass = '123456'


class OmiPay(object):

    def __init__(self, merchant_site_code, return_url, receiver,
                 transaction_info, order_code, price, currency, quantity,
                 tax, discount, fee_cal, fee_shipping, order_description,
                 buyer_info, affiliate_code, installment, inpage, payment_method_id,
                 token, token_type):
        self.merchant_site_code = str(merchant_site_code)
        self.return_url = str(return_url)
        self.receiver = str(receiver)
        self.transaction_info = str(transaction_info)
        self.order_code = str(order_code)
        self.price = str(price)
        self.currency = str(currency)
        self.quantity = str(quantity)
        self.tax = str(tax)
        self.discount = str(discount)
        self.fee_cal = str(fee_cal)
        self.fee_shipping = str(fee_shipping)
        self.order_description = str(order_description)
        self.buyer_info = str(buyer_info)
        self.affiliate_code = str(affiliate_code)
        self.installment = str(installment)
        self.inpage = str(inpage)
        self.payment_method_id = str(payment_method_id)
        self.token = str(token)
        self.token_type = str(token_type)

    def dict_prams(self):
        dict_obj = {
            'merchant_site_code': self.merchant_site_code,
            'return_url': self.return_url,
            'receiver': self.receiver,
            'transaction_info': self.transaction_info,
            'order_code': self.order_code,
            'price': self.price,
            'currency': self.currency,
            'quantity': self.quantity,
            'tax': self.tax,
            'discount': self.discount,
            'fee_cal': self.fee_cal,
            'fee_shipping': self.fee_shipping,
            'order_description': self.order_description,
            'buyer_info': self.buyer_info,
            'affiliate_code': self.affiliate_code,
            'installment': self.installment,
            'inpage': self.inpage,
            'payment_method_id': self.payment_method_id,
            'secure_code': ''
        }
        return dict_obj

    def generate_secure_code(self):
        secure_string = (self.merchant_site_code, self.return_url, self.receiver, self.transaction_info,
                         self.order_code, self.price, self.currency, self.quantity, self.tax, self.discount,
                         self.fee_cal, self.fee_shipping, self.order_description, self.buyer_info, self.affiliate_code,
                         self.installment, self.inpage, self.payment_method_id, secure_pass)
        secure_code = ' '.join(secure_string)
        return hashlib.md5(secure_code.encode('utf-8')).hexdigest()

    def render_url(self):
        url = ''
        unsecure_string = self.generate_secure_code()
        input_build_url = self.dict_prams()
        input_build_url['secure_code'] = unsecure_string
        for key, value in input_build_url.items():
            if url == '':
                url += key + '=' + value
            else:
                url += '&' + key + '=' + value
        return omipay_url + "?" + url


if __name__ == '__main__':
    url_obj = OmiPay(64916, 'https://checkout-sandbox.omipay.vn/test_checkout/checkout_v1/Fsuccess.php',
                     'vanmt@htpgroup.com.vn', 'tichhopthanhtoan', 'OM_1656422065', 20000, 'vnd', 1, 0, 0, 0, 0,
                     'Thanh+toán+đơn+hàng+OM_1656422065', '', '', 0, 0, 0, '', '')
    checkout_url = url_obj.render_url()
    print(checkout_url)

