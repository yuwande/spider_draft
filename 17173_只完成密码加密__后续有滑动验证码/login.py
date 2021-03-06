"""
Base_Url: https://www.17173.com/
Author: jing
Modify: 2020/10/22
"""
import execjs
import requests


class Login():
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def get_pwd(self):

        js_pwd = """
 hexMd5 = function(pwd) {
            function a(a) {
                return c(b(d(a)))
            }
            function b(a) {
                return f(g(e(a), 8 * a.length))
            }
            function c(a) {
                try {} catch (b) {
                    o = 0
                }
                for (var c, d = o ? "0123456789ABCDEF" : "0123456789abcdef", e = "", f = 0; f < a.length; f++)
                    c = a.charCodeAt(f),
                    e += d.charAt(c >>> 4 & 15) + d.charAt(15 & c);
                return e
            }
            function d(a) {
                for (var b, c, d = "", e = -1; ++e < a.length; )
                    b = a.charCodeAt(e),
                    c = e + 1 < a.length ? a.charCodeAt(e + 1) : 0,
                    b >= 55296 && 56319 >= b && c >= 56320 && 57343 >= c && (b = 65536 + ((1023 & b) << 10) + (1023 & c),
                    e++),
                    127 >= b ? d += String.fromCharCode(b) : 2047 >= b ? d += String.fromCharCode(192 | b >>> 6 & 31, 128 | 63 & b) : 65535 >= b ? d += String.fromCharCode(224 | b >>> 12 & 15, 128 | b >>> 6 & 63, 128 | 63 & b) : 2097151 >= b && (d += String.fromCharCode(240 | b >>> 18 & 7, 128 | b >>> 12 & 63, 128 | b >>> 6 & 63, 128 | 63 & b));
                return d
            }
            function e(a) {
                for (var b = Array(a.length >> 2), c = 0; c < b.length; c++)
                    b[c] = 0;
                for (var c = 0; c < 8 * a.length; c += 8)
                    b[c >> 5] |= (255 & a.charCodeAt(c / 8)) << c % 32;
                return b
            }
            function f(a) {
                for (var b = "", c = 0; c < 32 * a.length; c += 8)
                    b += String.fromCharCode(a[c >> 5] >>> c % 32 & 255);
                return b
            }
            function g(a, b) {
                a[b >> 5] |= 128 << b % 32,
                a[(b + 64 >>> 9 << 4) + 14] = b;
                for (var c = 1732584193, d = -271733879, e = -1732584194, f = 271733878, g = 0; g < a.length; g += 16) {
                    var h = c
                      , n = d
                      , o = e
                      , p = f;
                    c = i(c, d, e, f, a[g + 0], 7, -680876936),
                    f = i(f, c, d, e, a[g + 1], 12, -389564586),
                    e = i(e, f, c, d, a[g + 2], 17, 606105819),
                    d = i(d, e, f, c, a[g + 3], 22, -1044525330),
                    c = i(c, d, e, f, a[g + 4], 7, -176418897),
                    f = i(f, c, d, e, a[g + 5], 12, 1200080426),
                    e = i(e, f, c, d, a[g + 6], 17, -1473231341),
                    d = i(d, e, f, c, a[g + 7], 22, -45705983),
                    c = i(c, d, e, f, a[g + 8], 7, 1770035416),
                    f = i(f, c, d, e, a[g + 9], 12, -1958414417),
                    e = i(e, f, c, d, a[g + 10], 17, -42063),
                    d = i(d, e, f, c, a[g + 11], 22, -1990404162),
                    c = i(c, d, e, f, a[g + 12], 7, 1804603682),
                    f = i(f, c, d, e, a[g + 13], 12, -40341101),
                    e = i(e, f, c, d, a[g + 14], 17, -1502002290),
                    d = i(d, e, f, c, a[g + 15], 22, 1236535329),
                    c = j(c, d, e, f, a[g + 1], 5, -165796510),
                    f = j(f, c, d, e, a[g + 6], 9, -1069501632),
                    e = j(e, f, c, d, a[g + 11], 14, 643717713),
                    d = j(d, e, f, c, a[g + 0], 20, -373897302),
                    c = j(c, d, e, f, a[g + 5], 5, -701558691),
                    f = j(f, c, d, e, a[g + 10], 9, 38016083),
                    e = j(e, f, c, d, a[g + 15], 14, -660478335),
                    d = j(d, e, f, c, a[g + 4], 20, -405537848),
                    c = j(c, d, e, f, a[g + 9], 5, 568446438),
                    f = j(f, c, d, e, a[g + 14], 9, -1019803690),
                    e = j(e, f, c, d, a[g + 3], 14, -187363961),
                    d = j(d, e, f, c, a[g + 8], 20, 1163531501),
                    c = j(c, d, e, f, a[g + 13], 5, -1444681467),
                    f = j(f, c, d, e, a[g + 2], 9, -51403784),
                    e = j(e, f, c, d, a[g + 7], 14, 1735328473),
                    d = j(d, e, f, c, a[g + 12], 20, -1926607734),
                    c = k(c, d, e, f, a[g + 5], 4, -378558),
                    f = k(f, c, d, e, a[g + 8], 11, -2022574463),
                    e = k(e, f, c, d, a[g + 11], 16, 1839030562),
                    d = k(d, e, f, c, a[g + 14], 23, -35309556),
                    c = k(c, d, e, f, a[g + 1], 4, -1530992060),
                    f = k(f, c, d, e, a[g + 4], 11, 1272893353),
                    e = k(e, f, c, d, a[g + 7], 16, -155497632),
                    d = k(d, e, f, c, a[g + 10], 23, -1094730640),
                    c = k(c, d, e, f, a[g + 13], 4, 681279174),
                    f = k(f, c, d, e, a[g + 0], 11, -358537222),
                    e = k(e, f, c, d, a[g + 3], 16, -722521979),
                    d = k(d, e, f, c, a[g + 6], 23, 76029189),
                    c = k(c, d, e, f, a[g + 9], 4, -640364487),
                    f = k(f, c, d, e, a[g + 12], 11, -421815835),
                    e = k(e, f, c, d, a[g + 15], 16, 530742520),
                    d = k(d, e, f, c, a[g + 2], 23, -995338651),
                    c = l(c, d, e, f, a[g + 0], 6, -198630844),
                    f = l(f, c, d, e, a[g + 7], 10, 1126891415),
                    e = l(e, f, c, d, a[g + 14], 15, -1416354905),
                    d = l(d, e, f, c, a[g + 5], 21, -57434055),
                    c = l(c, d, e, f, a[g + 12], 6, 1700485571),
                    f = l(f, c, d, e, a[g + 3], 10, -1894986606),
                    e = l(e, f, c, d, a[g + 10], 15, -1051523),
                    d = l(d, e, f, c, a[g + 1], 21, -2054922799),
                    c = l(c, d, e, f, a[g + 8], 6, 1873313359),
                    f = l(f, c, d, e, a[g + 15], 10, -30611744),
                    e = l(e, f, c, d, a[g + 6], 15, -1560198380),
                    d = l(d, e, f, c, a[g + 13], 21, 1309151649),
                    c = l(c, d, e, f, a[g + 4], 6, -145523070),
                    f = l(f, c, d, e, a[g + 11], 10, -1120210379),
                    e = l(e, f, c, d, a[g + 2], 15, 718787259),
                    d = l(d, e, f, c, a[g + 9], 21, -343485551),
                    c = m(c, h),
                    d = m(d, n),
                    e = m(e, o),
                    f = m(f, p)
                }
                return Array(c, d, e, f)
            }
            function h(a, b, c, d, e, f) {
                return m(n(m(m(b, a), m(d, f)), e), c)
            }
            function i(a, b, c, d, e, f, g) {
                return h(b & c | ~b & d, a, b, e, f, g)
            }
            function j(a, b, c, d, e, f, g) {
                return h(b & d | c & ~d, a, b, e, f, g)
            }
            function k(a, b, c, d, e, f, g) {
                return h(b ^ c ^ d, a, b, e, f, g)
            }
            function l(a, b, c, d, e, f, g) {
                return h(c ^ (b | ~d), a, b, e, f, g)
            }
            function m(a, b) {
                var c = (65535 & a) + (65535 & b)
                  , d = (a >> 16) + (b >> 16) + (c >> 16);
                return d << 16 | 65535 & c
            }
            function n(a, b) {
                return a << b | a >>> 32 - b
            }
            var o = 0;
            return a(pwd)
        }
        
function getpwd(pwd){
return hexMd5(pwd)

}

"""
        pwd = execjs.compile(js_pwd).call("getpwd", "1111")   # TODO: 输入密码
        return pwd

    def login_(self):
        pwd = self.get_pwd()
        print(pwd)


