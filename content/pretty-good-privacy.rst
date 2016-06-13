خصوصية جيد جدا
##############
:date: 2013-09-23 06:42
:slug: pretty-good-privacy
:status: published

قد لايهمك التنصت أو التجسس الذي يحدث من قبل وكالة الأمن القومي الأمريكية
(`NSA <http://en.wikipedia.org/wiki/National_Security_Agency>`__) لاي
سبب من الأسباب! لكن من الجيد معرفة أن هناك طرق تستطيع من خلاله حماية
خصوصيتك، سواء في تصفحك، مراسلتك و غيرها...

من طرق المراسلة الآمنة، إستخدام  "**خصوصية جيد جدا**" (`Pretty Good
Privacy <http://en.wikipedia.org/wiki/Pretty_Good_Privacy>`__) أو
كاختصار(PGP).  ببساطة (PGP) هو برنامج يقوم بتشفير الرسائل المرسلة إليك
بإستخدام **مفتاحك العمومي** (**public key**) قبل إرسالها إليك،
وبإستخدامك **لمفتاحك الخاص** (**private key**) يمكنك فك التشفير والإطلاع
على الرسالة.

|pretty-good-privacy|

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
::

  -----BEGIN PGP PUBLIC KEY BLOCK-----
  Version: Keybase OpenPGP v2.0.53
  Comment: https://keybase.io/crypto

  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
  =G+3F
  -----END PGP PUBLIC KEY BLOCK-----


الموقع الرسمي لإضافة
`Mailvelope <http://www.mailvelope.com/help>`__ يقدم شرح ممتاز
لكيفية إستخدام الإضافة والتعامل معها. وايضا فيديو من lifehacker يشرح
بشكل سريع استيراد المفتاح واستخدام الإضافة.

 

فيديو آخر من **hak5** يشرح بشكل مفصلة إضافة \ **Mailvelope** (الشرح
يبداء من الدقيقة 5 تقريباً)

.. youtube:: 4ba0K-DhoGo
    :class: youtube-16x9

----

`حقوق الصورة <http://www.pgpi.org/doc/pgpintro/>`__

.. |pretty-good-privacy| image:: {filename}/uploads/2013/pretty-good-privacy/pretty-good-privacy.gif
