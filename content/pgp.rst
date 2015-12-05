خصوصية جيد جدا
##############
:date: 2013-09-23 06:42
:slug: pgp
:status: published

قد لايهمك التنصت أو التجسس الذي يحدث من قبل وكالة الأمن القومي الأمريكية
(`NSA <http://en.wikipedia.org/wiki/National_Security_Agency>`__) لاي
سبب من الأسباب! لكن من الجيد معرفة أن هناك طرق تستطيع من خلاله حماية
خصوصيتك، سواء في تصفحك، مراسلتك و غيرها...

من طرق المراسلة الآمنة، إستخدام  "**خصوصية جيد جدا**" (`**Pretty Good
Privacy** <http://en.wikipedia.org/wiki/Pretty_Good_Privacy>`__) أو
كاختصار(PGP).  ببساطة (PGP) هو برنامج يقوم بتشفير الرسائل المرسلة إليك
بإستخدام **مفتاحك العمومي** (**public key**) قبل إرسالها إليك،
وبإستخدامك **لمفتاحك الخاص** (**private key**) يمكنك فك التشفير والإطلاع
على الرسالة.

|PGP|

هناك برامج PGP كثيرة، شخصياً استخدم إضافة \ **Mailvelope** لبساطتها
وسهولة إستخدامها وتعاملها المباشر مع مزودي خدمة البريد الإلكتروني
الشهيرة مثل (Gmail) و(Yahoo) و(Outlook.com). هناك خطوات أساسية يجب عملها
حتى نتمكن من أستخدام مثل هذا البرامج تركيب البرنامج أو الإضافة (برنامج
**Mailvelope**  حاليا يدعم
`كروم <https://chrome.google.com/webstore/detail/mailvelope/kajibbejlbohfaggdiogboambcijhkke>`__
وقريبا فايرفوكس) وتوليد المفاتيح الخاصة بك (**مفتاح عمومي** و **مفتاح
خاص**) و خطوة إختيارية هي إضافة مفتاحك العمومي في خادم للمفاتيح (Key
Server) مثل (`MIT PGP Public Key Server <http://pgp.mit.edu/>`__) أو
(`SKS OpenPGP Key server <http://pool.sks-keyservers.net/>`__) أو غيرهم
حتى يتمكن الجميع من مراسلتك بطريقة آمنة. إضافة **Mailvelope** تقدم لك
إمكانية توليد مفاتيح خاصة بك أو إستيرادها في حالة كانت لديك مفاتيحك
الخاصة.

    مهم جداً الإنتباه بأن **المفتاح العامومي** (**public key**) هو الذي
    يتم نشرة وأن **المفتاح الخاص** (**private key**) يتم حفظه بسرية.

    .. raw:: html

       <p style="text-align: center;">

مفتاحي العامومي (**public key**)

    | -----BEGIN PGP PUBLIC KEY BLOCK-----
    |  Version: OpenPGP.js v.1.20130820
    |  Comment: http://openpgpjs.org

    | xsFNBFI/q84BEAC0/XgVdYMKstJWsp+HSzuOb8Heb86Gw4RgCyZezo0yLGh9
    |  oTMfJtM0LwVAw7rq6/CYa+z4uFEkcgvixvOnPz5VDzhAhoMzP7NmI042qIJY
    |  h93H2Zh+Mfgdqjxdld7W3mJhLJFByoCE7t7wiAG+981ozAkcl0KR5dCh78LS
    |  MQ3l3Jfce5gi/6vtKBYaYgmPj9WIRyE21pIKJr6LP4BBJPh4XeHL5homA+Oe
    |  W8jYV0KePv/n+cpGV3PDj1DBXW3JEjbCKbtcIb16FXh3VNxMB4R64uKkfgmF
    |  r/1/D0G0CzRJflNmk0ye7JXqMfdty9AmntvNj92DYMR5EcYuXa7Lxhe9WEOq
    |  VuBbCxlAKlYQHtXZ8LdWKWJE2uYwTVzVRYzdFEPclN0yRXT7aV0OueZBMB4f
    |  VbiTJX/yAZdBsFkxx9qvgIB2ZZy0LDtJNYK/OL21ruOUMypr4hisQjF+YTIS
    |  EQh6RxZ6hlvX36HxGnyPGa6k9xYtAP6zGfpoTrINbwPOmNHwBlbH87HLbCW2
    |  s8Ks1o9zN+h5nqHz1OAcRtrXQ4NHds6WzCDq65/eOhBawky6lfIlks+ydIOD
    |  g1yPOz/6GHH63YCgRasRo4lVPffU+tHwWCyeUTCEZ9Lx4/5vGMcwlbejGIMR
    |  xgO+vPVWgm3IZ2Umwxg4ajaOHOrnaKhboH6MXQARAQABzSJLaGFsaWQgQWxu
    |  dWFpbSA8a2FsdWFpbUBnbWFpbC5jb20+wsFcBBABCAAQBQJSP6wfCRCPRyMf
    |  fPLoOgAAdCsP/jck9A7H+rZ/v1AYoHPMNDnfcDJYDk9k8OgmywSM9fIIyzMk
    |  g3PSDUQAsBqPsoCwmXFYOj3euJHygf0IXzCs1DKKgxf5a/seDcuEwjNx5K19
    |  8nZYrZNN0RYQMvevYia7GnFcYxx3MkJ5vsbUaiXMRNVNykdPZSIGTvBVgmLc
    |  ipGG2fndH61N45VmtK7Lq8fVmU9cq7jTHAeuWK3DXUy5QhY692flzMeLoUuP
    |  CeTkiqPPMANPB2xKkQ+PguIxvo+M4fSCV88b7N/BHp2yEeb7Jxc9G4xyYuGK
    |  CcH0wT0nEUFLsHn6USmzjNsWTkYVp7wQU36o/RAxT/fW6+h/JjeXLNPYpVLR
    |  kygApYLZE/oBNmLA23l9SU4SvYmVqQKUano1Tk2/v7p+W1r4X2cFbC+LgX12
    |  JCK9nRs2fwkOiJyCJJUUN/V5vgJfRZunNleIdVrb4FXXwi2v62JWooOs4XM1
    |  9oL7rlm+CcZmlUsGGBIPDO/SR4F4q1bv0iwMMKXruGUY5S1yIYV5n5BQFdUJ
    |  b1VT5cN2I3haPvcFRAlTz4FzCYKb/v1ACPCaIXMD+dHHYQYUhMtKu8L42ZlP
    |  8xHWcHSFNSM6/hHIRLyF9Pe0szxuzNwiE/TwS7UdmTmW7umC1GGbx+hIRdWO
    |  nfIyAK6PPUOCjrW1oPWjKd//f671CQ0E7SRR
    |  =6F/v
    |  -----END PGP PUBLIC KEY BLOCK-----

    .. raw:: html

       <p style="text-align: left;">

 

الموقع الرسمي لإضافة
`**Mailvelope** <http://www.mailvelope.com/help>`__ يقدم شرح ممتاز
لكيفية إستخدام الإضافة والتعامل معها. وايضا فيديو من lifehacker يشرح
بشكل سريع استيراد المفتاح واستخدام الإضافة.

 

فيديو آخر من **hak5** يشرح بشكل مفصلة إضافة \ **Mailvelope** (الشرح
يبداء من الدقيقة 5 تقريباً)

--------------------------------------

`حقوق الصورة <http://www.pgpi.org/doc/pgpintro/>`__

.. |PGP| image:: http://blog.kalua.im/wp-content/uploads/2013/09/PGP.gif
