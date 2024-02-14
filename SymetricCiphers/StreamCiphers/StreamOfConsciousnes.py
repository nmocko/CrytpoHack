import requests
import operator


def xor_hex_strings(hex_str1, hex_str2):
    # Convert hex strings to bytes
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)

    m = min(len(bytes1), len(bytes2))

    # Perform XOR operation
    result_bytes = bytes(a ^ b for a, b in zip(bytes1[0:m], bytes2[0:m]))

    # Convert the result back to a hex string
    result_hex_str = result_bytes.decode()

    return result_hex_str


tab = [{} for _ in range(6)]
stats = "etaoin"

data = ['b8c5648ecff80dd8f4b90dec5ea95113132b6d4595e6de5d55f4f974388e04c0800c6edc11e918582970c14f71',
        'b8913785cffa468cb8b41ba90aa35518413d6c59d0a8db0840baf4207682118ec70b7fdc10e71b173974c60a',
        'bd8a618382b4118af7b41feb12b51856353a7c54dcecd61313eebd3f388e07c08f066ddc1df210193968824d2b26c105f5b960d7f64030ecc981d46d4747d79031f6017a55b9e720157f6cfa715edf7584b615e96e659520c714359a1a',
        'b8c27ac6dbfa0999e8a607a55e85071204217c5f8aed991440b6bd203e845086861c76885ef35515227fc7087f64dd02f9d02fd5a11536f1c598c87d0652d29276ac473155beee2850123af77a47ca7588bd5f',
        '92976e96dafb1a93abaf4bbe0cff131b3e202a58c9bbe64c01c5fb6061d51c9d',
        'b98a60c6dee60e8dfcf61fe71aec4f171122600d94ed9e1158baff31769618858949729959e7100c3831cf5d7f68c702bcb8',
        'a58d6583cbb40397e1a55efb0ba2491f0f35350d8ce4d8045df4fa7437955088881b69990aac552b2e63db4b256ec957',
        'b8c5648ecff80dd4b89f59e512ec4b19123739488aedcb0440f2f43a31c11986c7017fdc1def100b2536d6043c69c513f9fb69dbea4e',
        'be9065d98ec30981b8b90bfb41',
        'a58d7295cbb40997eaa51bfa52ec531e0821394e9dfacb1455fdf8747bc1188f904953dc15ef140c237482492675cd1abfb961d6a11430f0d7c8db655441d79f31bd0f7955b9e7204c1968fa3f4ad639c5b018ba362d9e39d74619d447295ad2ffe66f932603fe7a2af2f968e471b7c5675759d26ec1ce',
        'b096378fc8b428d8f0b71aa91fa25e56163b6a45dcfcd65d56ffbd3d38c10488824968951ee801596b5882473e688f02f8',
        'a180658ecfe412d8f0b35ee11fbf071b08216a4898a8cd1551bae92637881ec086077edc10f3551a2a72c9043d7f8818b6ee2698d60136ed8485d7764313d68b3bb1433d14b9e62a5b1f',
        'a68a628acab428d8f0b708ec5eae421a08376f4898a8cd1551f4bd203e8004c0ae4979930cec11583974c3473726db03baf128dce4102cf1d7c8d762065bcb933fb4463501a4e02b0a',
        'a58d72c6daf1138af1b412ec5eb84f1f0f3539448fa8cd1555eebd203e845090861a6edc1ae11b5f3f31c0417f72c704b7b967cdf5403ae08481cc770641d19122ab01',
        'a68d76928ef54196f9a50af05ebf4a130d3e395994e1ca5d44fbf43a22c118818347',
        'b39063c6e7b41691f4ba5efa16a35056093b7403',
        'bf8a3bc6e7b30d94b8b111a917a207020e725d4290e4c05d55f4f97422841c8cc7017f8e59f3010a2a78c54c2b26c703ad',
        'b58a7b8ad7b41691f4ba5efd16a5491d4126714c88a8f05a59baf1313797198e80497bdc0ae516172575824c2a75ca17b7fd28d9ef0478edcc89cc24525bdb8c33be402610edc665584b69eb3f58cf2780b408e96f68dc25cd46249c51614cccfca866d8',
        'a68d76928ef54194f7a25ee618ec531e083c7e5edcfcd11c40bae93c338f5093820c77991da001176b7cc7042c69881bb8eb7edded0c37ecd7c8d96a4213cb9037ac5b351ca3ee27595b36bf774acc30c5ba14aa6260996cca08239d532f52d8faa56098244aac3b37f3bc3cf87cf2dc2f5f50d4748fa92da5730f18b904a1cbf57534ed4393f668ccd755fb360203d80434c04e4b481cddff7780ad9afcf6',
        'b5977295ddb90c99f3bf10ee5ead4912411f704190e1d71846e3',
        'a68d6ec6cafb418cf0b307a919a307190f72694c95e6cd145afdbd35388550829200769810ee12582a7dce042b6ecd56adf065ddbe',
        'b08b73c6e7b41290f9ba12a917ab49191337394488a6']

key = 'f1e517e6ae9461f898d67e897ecc27766152192dfc88b97d349a9d5456e170e0e7691afc798075784b11a2245f06a876d9'
len_key = len(key)
dat = data[10]
letter = 's'

# next_key = int(dat[len_key: len_key + 2], 16) ^ ord(letter)
# print(hex(next_key))
for i in range(22):
    dat = data[i]
    print(xor_hex_strings(key, dat))

# for itr in range(22):
#
#     ct = data[itr]
#
#     l = len(ct) // 2
#
#     if l > 6:
#         l = 6
#
#     for i in range(l):
#
#         if ct[2*i: 2*i + 2] in tab[i]:
#             tab[i][ct[2*i: 2*i + 2]] += 1
#
#         else:
#             tab[i][ct[2 * i: 2 * i + 2]] = 1
#
# print(tab)
# whole_key = ''
# tab[1] = dict(sorted(tab[1].items(), key=operator.itemgetter(1), reverse=True))
# common = list(tab[1].keys())[0]
#
# for i in range(6):
#     key = int(common, 16) ^ ord(stats[i])
#     whole_key += f'{key:0>2X}'
#     for j in tab[1]:
#         print("int = ", int(j, 16), "key = ", key, "xor = ", int(j, 16) ^ key, "number =", tab[1][j])
#
#         xor = int(j, 16) ^ key
#         if xor < 97 or xor > 122:
#             print(xor)
#
#     print('=' * 22)

