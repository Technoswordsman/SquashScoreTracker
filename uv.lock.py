version = 1
requires-python = ">=3.11"
resolution-markers = [
    "python_full_version >= '3.12'",
    "python_full_version < '3.12'",
]

[[package]]
name = "altair"
version = "5.5.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jinja2" },
    { name = "jsonschema" },
    { name = "narwhals" },
    { name = "packaging" },
    { name = "typing-extensions", marker = "python_full_version < '3.14'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/16/b1/f2969c7bdb8ad8bbdda031687defdce2c19afba2aa2c8e1d2a17f78376d8/altair-5.5.0.tar.gz", hash = "sha256:d960ebe6178c56de3855a68c47b516be38640b73fb3b5111c2a9ca90546dd73d", size = 705305 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/aa/f3/0b6ced594e51cc95d8c1fc1640d3623770d01e4969d29c0bd09945fafefa/altair-5.5.0-py3-none-any.whl", hash = "sha256:91a310b926508d560fe0148d02a194f38b824122641ef528113d029fcd129f8c", size = 731200 },
]

[[package]]
name = "attrs"
version = "25.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/49/7c/fdf464bcc51d23881d110abd74b512a42b3d5d376a55a831b44c603ae17f/attrs-25.1.0.tar.gz", hash = "sha256:1c97078a80c814273a76b2a298a932eb681c87415c11dee0a6921de7f1b02c3e", size = 810562 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fc/30/d4986a882011f9df997a55e6becd864812ccfcd821d64aac8570ee39f719/attrs-25.1.0-py3-none-any.whl", hash = "sha256:c75a69e28a550a7e93789579c22aa26b0f5b83b75dc4e08fe092980051e1090a", size = 63152 },
]

[[package]]
name = "blinker"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/21/28/9b3f50ce0e048515135495f198351908d99540d69bfdc8c1d15b73dc55ce/blinker-1.9.0.tar.gz", hash = "sha256:b4ce2265a7abece45e7cc896e98dbebe6cead56bcf805a3d23136d145f5445bf", size = 22460 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/10/cb/f2ad4230dc2eb1a74edf38f1a38b9b52277f75bef262d8908e60d957e13c/blinker-1.9.0-py3-none-any.whl", hash = "sha256:ba0efaa9080b619ff2f3459d1d500c57bddea4a6b424b60a91141db6fd2f08bc", size = 8458 },
]

[[package]]
name = "cachetools"
version = "5.5.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6c/81/3747dad6b14fa2cf53fcf10548cf5aea6913e96fab41a3c198676f8948a5/cachetools-5.5.2.tar.gz", hash = "sha256:1a661caa9175d26759571b2e19580f9d6393969e5dfca11fdb1f947a23e640d4", size = 28380 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/72/76/20fa66124dbe6be5cafeb312ece67de6b61dd91a0247d1ea13db4ebb33c2/cachetools-5.5.2-py3-none-any.whl", hash = "sha256:d26a22bcc62eb95c3beabd9f1ee5e820d3d2704fe2967cbe350e20c8ffcd3f0a", size = 10080 },
]

[[package]]
name = "certifi"
version = "2025.1.31"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1c/ab/c9f1e32b7b1bf505bf26f0ef697775960db7932abeb7b516de930ba2705f/certifi-2025.1.31.tar.gz", hash = "sha256:3d5da6925056f6f18f119200434a4780a94263f10d1c21d032a6f6b2baa20651", size = 167577 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/fc/bce832fd4fd99766c04d1ee0eead6b0ec6486fb100ae5e74c1d91292b982/certifi-2025.1.31-py3-none-any.whl", hash = "sha256:ca78db4565a652026a4db2bcdf68f2fb589ea80d0be70e03929ed730746b84fe", size = 166393 },
]

[[package]]
name = "chardet"
version = "5.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/0d/f7b6ab21ec75897ed80c17d79b15951a719226b9fababf1e40ea74d69079/chardet-5.2.0.tar.gz", hash = "sha256:1b3b6ff479a8c414bc3fa2c0852995695c4a026dcd6d0633b2dd092ca39c1cf7", size = 2069618 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/6f/f5fbc992a329ee4e0f288c1fe0e2ad9485ed064cac731ed2fe47dcc38cbf/chardet-5.2.0-py3-none-any.whl", hash = "sha256:e1cf59446890a00105fe7b7912492ea04b6e6f06d4b742b2c788469e34c82970", size = 199385 },
]

[[package]]
name = "charset-normalizer"
version = "3.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/16/b0/572805e227f01586461c80e0fd25d65a2115599cc9dad142fee4b747c357/charset_normalizer-3.4.1.tar.gz", hash = "sha256:44251f18cd68a75b56585dd00dae26183e102cd5e0f9f1466e6df5da2ed64ea3", size = 123188 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/72/80/41ef5d5a7935d2d3a773e3eaebf0a9350542f2cab4eac59a7a4741fbbbbe/charset_normalizer-3.4.1-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:8bfa33f4f2672964266e940dd22a195989ba31669bd84629f05fab3ef4e2d125", size = 194995 },
    { url = "https://files.pythonhosted.org/packages/7a/28/0b9fefa7b8b080ec492110af6d88aa3dea91c464b17d53474b6e9ba5d2c5/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:28bf57629c75e810b6ae989f03c0828d64d6b26a5e205535585f96093e405ed1", size = 139471 },
    { url = "https://files.pythonhosted.org/packages/71/64/d24ab1a997efb06402e3fc07317e94da358e2585165930d9d59ad45fcae2/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f08ff5e948271dc7e18a35641d2f11a4cd8dfd5634f55228b691e62b37125eb3", size = 149831 },
    { url = "https://files.pythonhosted.org/packages/37/ed/be39e5258e198655240db5e19e0b11379163ad7070962d6b0c87ed2c4d39/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:234ac59ea147c59ee4da87a0c0f098e9c8d169f4dc2a159ef720f1a61bbe27cd", size = 142335 },
    { url = "https://files.pythonhosted.org/packages/88/83/489e9504711fa05d8dde1574996408026bdbdbd938f23be67deebb5eca92/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd4ec41f914fa74ad1b8304bbc634b3de73d2a0889bd32076342a573e0779e00", size = 143862 },
    { url = "https://files.pythonhosted.org/packages/c6/c7/32da20821cf387b759ad24627a9aca289d2822de929b8a41b6241767b461/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:eea6ee1db730b3483adf394ea72f808b6e18cf3cb6454b4d86e04fa8c4327a12", size = 145673 },
    { url = "https://files.pythonhosted.org/packages/68/85/f4288e96039abdd5aeb5c546fa20a37b50da71b5cf01e75e87f16cd43304/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c96836c97b1238e9c9e3fe90844c947d5afbf4f4c92762679acfe19927d81d77", size = 140211 },
    { url = "https://files.pythonhosted.org/packages/28/a3/a42e70d03cbdabc18997baf4f0227c73591a08041c149e710045c281f97b/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:4d86f7aff21ee58f26dcf5ae81a9addbd914115cdebcbb2217e4f0ed8982e146", size = 148039 },
    { url = "https://files.pythonhosted.org/packages/85/e4/65699e8ab3014ecbe6f5c71d1a55d810fb716bbfd74f6283d5c2aa87febf/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:09b5e6733cbd160dcc09589227187e242a30a49ca5cefa5a7edd3f9d19ed53fd", size = 151939 },
    { url = "https://files.pythonhosted.org/packages/b1/82/8e9fe624cc5374193de6860aba3ea8070f584c8565ee77c168ec13274bd2/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:5777ee0881f9499ed0f71cc82cf873d9a0ca8af166dfa0af8ec4e675b7df48e6", size = 149075 },
    { url = "https://files.pythonhosted.org/packages/3d/7b/82865ba54c765560c8433f65e8acb9217cb839a9e32b42af4aa8e945870f/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:237bdbe6159cff53b4f24f397d43c6336c6b0b42affbe857970cefbb620911c8", size = 144340 },
    { url = "https://files.pythonhosted.org/packages/b5/b6/9674a4b7d4d99a0d2df9b215da766ee682718f88055751e1e5e753c82db0/charset_normalizer-3.4.1-cp311-cp311-win32.whl", hash = "sha256:8417cb1f36cc0bc7eaba8ccb0e04d55f0ee52df06df3ad55259b9a323555fc8b", size = 95205 },
    { url = "https://files.pythonhosted.org/packages/1e/ab/45b180e175de4402dcf7547e4fb617283bae54ce35c27930a6f35b6bef15/charset_normalizer-3.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:d7f50a1f8c450f3925cb367d011448c39239bb3eb4117c36a6d354794de4ce76", size = 102441 },
    { url = "https://files.pythonhosted.org/packages/0a/9a/dd1e1cdceb841925b7798369a09279bd1cf183cef0f9ddf15a3a6502ee45/charset_normalizer-3.4.1-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:73d94b58ec7fecbc7366247d3b0b10a21681004153238750bb67bd9012414545", size = 196105 },
    { url = "https://files.pythonhosted.org/packages/d3/8c/90bfabf8c4809ecb648f39794cf2a84ff2e7d2a6cf159fe68d9a26160467/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:dad3e487649f498dd991eeb901125411559b22e8d7ab25d3aeb1af367df5efd7", size = 140404 },
    { url = "https://files.pythonhosted.org/packages/ad/8f/e410d57c721945ea3b4f1a04b74f70ce8fa800d393d72899f0a40526401f/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c30197aa96e8eed02200a83fba2657b4c3acd0f0aa4bdc9f6c1af8e8962e0757", size = 150423 },
    { url = "https://files.pythonhosted.org/packages/f0/b8/e6825e25deb691ff98cf5c9072ee0605dc2acfca98af70c2d1b1bc75190d/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2369eea1ee4a7610a860d88f268eb39b95cb588acd7235e02fd5a5601773d4fa", size = 143184 },
    { url = "https://files.pythonhosted.org/packages/3e/a2/513f6cbe752421f16d969e32f3583762bfd583848b763913ddab8d9bfd4f/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bc2722592d8998c870fa4e290c2eec2c1569b87fe58618e67d38b4665dfa680d", size = 145268 },
    { url = "https://files.pythonhosted.org/packages/74/94/8a5277664f27c3c438546f3eb53b33f5b19568eb7424736bdc440a88a31f/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ffc9202a29ab3920fa812879e95a9e78b2465fd10be7fcbd042899695d75e616", size = 147601 },
    { url = "https://files.pythonhosted.org/packages/7c/5f/6d352c51ee763623a98e31194823518e09bfa48be2a7e8383cf691bbb3d0/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:804a4d582ba6e5b747c625bf1255e6b1507465494a40a2130978bda7b932c90b", size = 141098 },
    { url = "https://files.pythonhosted.org/packages/78/d4/f5704cb629ba5ab16d1d3d741396aec6dc3ca2b67757c45b0599bb010478/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:0f55e69f030f7163dffe9fd0752b32f070566451afe180f99dbeeb81f511ad8d", size = 149520 },
    { url = "https://files.pythonhosted.org/packages/c5/96/64120b1d02b81785f222b976c0fb79a35875457fa9bb40827678e54d1bc8/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:c4c3e6da02df6fa1410a7680bd3f63d4f710232d3139089536310d027950696a", size = 152852 },
    { url = "https://files.pythonhosted.org/packages/84/c9/98e3732278a99f47d487fd3468bc60b882920cef29d1fa6ca460a1fdf4e6/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:5df196eb874dae23dcfb968c83d4f8fdccb333330fe1fc278ac5ceeb101003a9", size = 150488 },
    { url = "https://files.pythonhosted.org/packages/13/0e/9c8d4cb99c98c1007cc11eda969ebfe837bbbd0acdb4736d228ccaabcd22/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e358e64305fe12299a08e08978f51fc21fac060dcfcddd95453eabe5b93ed0e1", size = 146192 },
    { url = "https://files.pythonhosted.org/packages/b2/21/2b6b5b860781a0b49427309cb8670785aa543fb2178de875b87b9cc97746/charset_normalizer-3.4.1-cp312-cp312-win32.whl", hash = "sha256:9b23ca7ef998bc739bf6ffc077c2116917eabcc901f88da1b9856b210ef63f35", size = 95550 },
    { url = "https://files.pythonhosted.org/packages/21/5b/1b390b03b1d16c7e382b561c5329f83cc06623916aab983e8ab9239c7d5c/charset_normalizer-3.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:6ff8a4a60c227ad87030d76e99cd1698345d4491638dfa6673027c48b3cd395f", size = 102785 },
    { url = "https://files.pythonhosted.org/packages/38/94/ce8e6f63d18049672c76d07d119304e1e2d7c6098f0841b51c666e9f44a0/charset_normalizer-3.4.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:aabfa34badd18f1da5ec1bc2715cadc8dca465868a4e73a0173466b688f29dda", size = 195698 },
    { url = "https://files.pythonhosted.org/packages/24/2e/dfdd9770664aae179a96561cc6952ff08f9a8cd09a908f259a9dfa063568/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:22e14b5d70560b8dd51ec22863f370d1e595ac3d024cb8ad7d308b4cd95f8313", size = 140162 },
    { url = "https://files.pythonhosted.org/packages/24/4e/f646b9093cff8fc86f2d60af2de4dc17c759de9d554f130b140ea4738ca6/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:8436c508b408b82d87dc5f62496973a1805cd46727c34440b0d29d8a2f50a6c9", size = 150263 },
    { url = "https://files.pythonhosted.org/packages/5e/67/2937f8d548c3ef6e2f9aab0f6e21001056f692d43282b165e7c56023e6dd/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2d074908e1aecee37a7635990b2c6d504cd4766c7bc9fc86d63f9c09af3fa11b", size = 142966 },
    { url = "https://files.pythonhosted.org/packages/52/ed/b7f4f07de100bdb95c1756d3a4d17b90c1a3c53715c1a476f8738058e0fa/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:955f8851919303c92343d2f66165294848d57e9bba6cf6e3625485a70a038d11", size = 144992 },
    { url = "https://files.pythonhosted.org/packages/96/2c/d49710a6dbcd3776265f4c923bb73ebe83933dfbaa841c5da850fe0fd20b/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:44ecbf16649486d4aebafeaa7ec4c9fed8b88101f4dd612dcaf65d5e815f837f", size = 147162 },
    { url = "https://files.pythonhosted.org/packages/b4/41/35ff1f9a6bd380303dea55e44c4933b4cc3c4850988927d4082ada230273/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:0924e81d3d5e70f8126529951dac65c1010cdf117bb75eb02dd12339b57749dd", size = 140972 },
    { url = "https://files.pythonhosted.org/packages/fb/43/c6a0b685fe6910d08ba971f62cd9c3e862a85770395ba5d9cad4fede33ab/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2967f74ad52c3b98de4c3b32e1a44e32975e008a9cd2a8cc8966d6a5218c5cb2", size = 149095 },
    { url = "https://files.pythonhosted.org/packages/4c/ff/a9a504662452e2d2878512115638966e75633519ec11f25fca3d2049a94a/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:c75cb2a3e389853835e84a2d8fb2b81a10645b503eca9bcb98df6b5a43eb8886", size = 152668 },
    { url = "https://files.pythonhosted.org/packages/6c/71/189996b6d9a4b932564701628af5cee6716733e9165af1d5e1b285c530ed/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:09b26ae6b1abf0d27570633b2b078a2a20419c99d66fb2823173d73f188ce601", size = 150073 },
    { url = "https://files.pythonhosted.org/packages/e4/93/946a86ce20790e11312c87c75ba68d5f6ad2208cfb52b2d6a2c32840d922/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:fa88b843d6e211393a37219e6a1c1df99d35e8fd90446f1118f4216e307e48cd", size = 145732 },
    { url = "https://files.pythonhosted.org/packages/cd/e5/131d2fb1b0dddafc37be4f3a2fa79aa4c037368be9423061dccadfd90091/charset_normalizer-3.4.1-cp313-cp313-win32.whl", hash = "sha256:eb8178fe3dba6450a3e024e95ac49ed3400e506fd4e9e5c32d30adda88cbd407", size = 95391 },
    { url = "https://files.pythonhosted.org/packages/27/f2/4f9a69cc7712b9b5ad8fdb87039fd89abba997ad5cbe690d1835d40405b0/charset_normalizer-3.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:b1ac5992a838106edb89654e0aebfc24f5848ae2547d22c2c3f66454daa11971", size = 102702 },
    { url = "https://files.pythonhosted.org/packages/0e/f6/65ecc6878a89bb1c23a086ea335ad4bf21a588990c3f535a227b9eea9108/charset_normalizer-3.4.1-py3-none-any.whl", hash = "sha256:d98b1668f06378c6dbefec3b92299716b931cd4e6061f3c875a71ced1780ab85", size = 49767 },
]

[[package]]
name = "click"
version = "8.1.8"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b9/2e/0090cbf739cee7d23781ad4b89a9894a41538e4fcf4c31dcdd705b78eb8b/click-8.1.8.tar.gz", hash = "sha256:ed53c9d8990d83c2a27deae68e4ee337473f6330c040a31d4225c9574d16096a", size = 226593 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/d4/7ebdbd03970677812aac39c869717059dbb71a4cfc033ca6e5221787892c/click-8.1.8-py3-none-any.whl", hash = "sha256:63c132bbbed01578a06712a2d1f497bb62d9c1c0d329b7903a866228027263b2", size = 98188 },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335 },
]

[[package]]
name = "gitdb"
version = "4.0.12"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "smmap" },
]
sdist = { url = "https://files.pythonhosted.org/packages/72/94/63b0fc47eb32792c7ba1fe1b694daec9a63620db1e313033d18140c2320a/gitdb-4.0.12.tar.gz", hash = "sha256:5ef71f855d191a3326fcfbc0d5da835f26b13fbcba60c32c21091c349ffdb571", size = 394684 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/61/5c78b91c3143ed5c14207f463aecfc8f9dbb5092fb2869baf37c273b2705/gitdb-4.0.12-py3-none-any.whl", hash = "sha256:67073e15955400952c6565cc3e707c554a4eea2e428946f7a4c162fab9bd9bcf", size = 62794 },
]

[[package]]
name = "gitpython"
version = "3.1.44"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "gitdb" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c0/89/37df0b71473153574a5cdef8f242de422a0f5d26d7a9e231e6f169b4ad14/gitpython-3.1.44.tar.gz", hash = "sha256:c87e30b26253bf5418b01b0660f818967f3c503193838337fe5e573331249269", size = 214196 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1d/9a/4114a9057db2f1462d5c8f8390ab7383925fe1ac012eaa42402ad65c2963/GitPython-3.1.44-py3-none-any.whl", hash = "sha256:9e0e10cda9bed1ee64bc9a6de50e7e38a9c9943241cd7f585f6df3ed28011110", size = 207599 },
]

[[package]]
name = "greenlet"
version = "3.1.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2f/ff/df5fede753cc10f6a5be0931204ea30c35fa2f2ea7a35b25bdaf4fe40e46/greenlet-3.1.1.tar.gz", hash = "sha256:4ce3ac6cdb6adf7946475d7ef31777c26d94bccc377e070a7986bd2d5c515467", size = 186022 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/28/62/1c2665558618553c42922ed47a4e6d6527e2fa3516a8256c2f431c5d0441/greenlet-3.1.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:e4d333e558953648ca09d64f13e6d8f0523fa705f51cae3f03b5983489958c70", size = 272479 },
    { url = "https://files.pythonhosted.org/packages/76/9d/421e2d5f07285b6e4e3a676b016ca781f63cfe4a0cd8eaecf3fd6f7a71ae/greenlet-3.1.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:09fc016b73c94e98e29af67ab7b9a879c307c6731a2c9da0db5a7d9b7edd1159", size = 640404 },
    { url = "https://files.pythonhosted.org/packages/e5/de/6e05f5c59262a584e502dd3d261bbdd2c97ab5416cc9c0b91ea38932a901/greenlet-3.1.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d5e975ca70269d66d17dd995dafc06f1b06e8cb1ec1e9ed54c1d1e4a7c4cf26e", size = 652813 },
    { url = "https://files.pythonhosted.org/packages/49/93/d5f93c84241acdea15a8fd329362c2c71c79e1a507c3f142a5d67ea435ae/greenlet-3.1.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3b2813dc3de8c1ee3f924e4d4227999285fd335d1bcc0d2be6dc3f1f6a318ec1", size = 648517 },
    { url = "https://files.pythonhosted.org/packages/15/85/72f77fc02d00470c86a5c982b8daafdf65d38aefbbe441cebff3bf7037fc/greenlet-3.1.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e347b3bfcf985a05e8c0b7d462ba6f15b1ee1c909e2dcad795e49e91b152c383", size = 647831 },
    { url = "https://files.pythonhosted.org/packages/f7/4b/1c9695aa24f808e156c8f4813f685d975ca73c000c2a5056c514c64980f6/greenlet-3.1.1-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9e8f8c9cb53cdac7ba9793c276acd90168f416b9ce36799b9b885790f8ad6c0a", size = 602413 },
    { url = "https://files.pythonhosted.org/packages/76/70/ad6e5b31ef330f03b12559d19fda2606a522d3849cde46b24f223d6d1619/greenlet-3.1.1-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:62ee94988d6b4722ce0028644418d93a52429e977d742ca2ccbe1c4f4a792511", size = 1129619 },
    { url = "https://files.pythonhosted.org/packages/f4/fb/201e1b932e584066e0f0658b538e73c459b34d44b4bd4034f682423bc801/greenlet-3.1.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:1776fd7f989fc6b8d8c8cb8da1f6b82c5814957264d1f6cf818d475ec2bf6395", size = 1155198 },
    { url = "https://files.pythonhosted.org/packages/12/da/b9ed5e310bb8b89661b80cbcd4db5a067903bbcd7fc854923f5ebb4144f0/greenlet-3.1.1-cp311-cp311-win_amd64.whl", hash = "sha256:48ca08c771c268a768087b408658e216133aecd835c0ded47ce955381105ba39", size = 298930 },
    { url = "https://files.pythonhosted.org/packages/7d/ec/bad1ac26764d26aa1353216fcbfa4670050f66d445448aafa227f8b16e80/greenlet-3.1.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:4afe7ea89de619adc868e087b4d2359282058479d7cfb94970adf4b55284574d", size = 274260 },
    { url = "https://files.pythonhosted.org/packages/66/d4/c8c04958870f482459ab5956c2942c4ec35cac7fe245527f1039837c17a9/greenlet-3.1.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f406b22b7c9a9b4f8aa9d2ab13d6ae0ac3e85c9a809bd590ad53fed2bf70dc79", size = 649064 },
    { url = "https://files.pythonhosted.org/packages/51/41/467b12a8c7c1303d20abcca145db2be4e6cd50a951fa30af48b6ec607581/greenlet-3.1.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c3a701fe5a9695b238503ce5bbe8218e03c3bcccf7e204e455e7462d770268aa", size = 663420 },
    { url = "https://files.pythonhosted.org/packages/27/8f/2a93cd9b1e7107d5c7b3b7816eeadcac2ebcaf6d6513df9abaf0334777f6/greenlet-3.1.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2846930c65b47d70b9d178e89c7e1a69c95c1f68ea5aa0a58646b7a96df12441", size = 658035 },
    { url = "https://files.pythonhosted.org/packages/57/5c/7c6f50cb12be092e1dccb2599be5a942c3416dbcfb76efcf54b3f8be4d8d/greenlet-3.1.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:99cfaa2110534e2cf3ba31a7abcac9d328d1d9f1b95beede58294a60348fba36", size = 660105 },
    { url = "https://files.pythonhosted.org/packages/f1/66/033e58a50fd9ec9df00a8671c74f1f3a320564c6415a4ed82a1c651654ba/greenlet-3.1.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1443279c19fca463fc33e65ef2a935a5b09bb90f978beab37729e1c3c6c25fe9", size = 613077 },
    { url = "https://files.pythonhosted.org/packages/19/c5/36384a06f748044d06bdd8776e231fadf92fc896bd12cb1c9f5a1bda9578/greenlet-3.1.1-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:b7cede291382a78f7bb5f04a529cb18e068dd29e0fb27376074b6d0317bf4dd0", size = 1135975 },
    { url = "https://files.pythonhosted.org/packages/38/f9/c0a0eb61bdf808d23266ecf1d63309f0e1471f284300ce6dac0ae1231881/greenlet-3.1.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:23f20bb60ae298d7d8656c6ec6db134bca379ecefadb0b19ce6f19d1f232a942", size = 1163955 },
    { url = "https://files.pythonhosted.org/packages/43/21/a5d9df1d21514883333fc86584c07c2b49ba7c602e670b174bd73cfc9c7f/greenlet-3.1.1-cp312-cp312-win_amd64.whl", hash = "sha256:7124e16b4c55d417577c2077be379514321916d5790fa287c9ed6f23bd2ffd01", size = 299655 },
    { url = "https://files.pythonhosted.org/packages/f3/57/0db4940cd7bb461365ca8d6fd53e68254c9dbbcc2b452e69d0d41f10a85e/greenlet-3.1.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:05175c27cb459dcfc05d026c4232f9de8913ed006d42713cb8a5137bd49375f1", size = 272990 },
    { url = "https://files.pythonhosted.org/packages/1c/ec/423d113c9f74e5e402e175b157203e9102feeb7088cee844d735b28ef963/greenlet-3.1.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:935e943ec47c4afab8965954bf49bfa639c05d4ccf9ef6e924188f762145c0ff", size = 649175 },
    { url = "https://files.pythonhosted.org/packages/a9/46/ddbd2db9ff209186b7b7c621d1432e2f21714adc988703dbdd0e65155c77/greenlet-3.1.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:667a9706c970cb552ede35aee17339a18e8f2a87a51fba2ed39ceeeb1004798a", size = 663425 },
    { url = "https://files.pythonhosted.org/packages/bc/f9/9c82d6b2b04aa37e38e74f0c429aece5eeb02bab6e3b98e7db89b23d94c6/greenlet-3.1.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b8a678974d1f3aa55f6cc34dc480169d58f2e6d8958895d68845fa4ab566509e", size = 657736 },
    { url = "https://files.pythonhosted.org/packages/d9/42/b87bc2a81e3a62c3de2b0d550bf91a86939442b7ff85abb94eec3fc0e6aa/greenlet-3.1.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:efc0f674aa41b92da8c49e0346318c6075d734994c3c4e4430b1c3f853e498e4", size = 660347 },
    { url = "https://files.pythonhosted.org/packages/37/fa/71599c3fd06336cdc3eac52e6871cfebab4d9d70674a9a9e7a482c318e99/greenlet-3.1.1-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0153404a4bb921f0ff1abeb5ce8a5131da56b953eda6e14b88dc6bbc04d2049e", size = 615583 },
    { url = "https://files.pythonhosted.org/packages/4e/96/e9ef85de031703ee7a4483489b40cf307f93c1824a02e903106f2ea315fe/greenlet-3.1.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:275f72decf9932639c1c6dd1013a1bc266438eb32710016a1c742df5da6e60a1", size = 1133039 },
    { url = "https://files.pythonhosted.org/packages/87/76/b2b6362accd69f2d1889db61a18c94bc743e961e3cab344c2effaa4b4a25/greenlet-3.1.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:c4aab7f6381f38a4b42f269057aee279ab0fc7bf2e929e3d4abfae97b682a12c", size = 1160716 },
    { url = "https://files.pythonhosted.org/packages/1f/1b/54336d876186920e185066d8c3024ad55f21d7cc3683c856127ddb7b13ce/greenlet-3.1.1-cp313-cp313-win_amd64.whl", hash = "sha256:b42703b1cf69f2aa1df7d1030b9d77d3e584a70755674d60e710f0af570f3761", size = 299490 },
    { url = "https://files.pythonhosted.org/packages/5f/17/bea55bf36990e1638a2af5ba10c1640273ef20f627962cf97107f1e5d637/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f1695e76146579f8c06c1509c7ce4dfe0706f49c6831a817ac04eebb2fd02011", size = 643731 },
    { url = "https://files.pythonhosted.org/packages/78/d2/aa3d2157f9ab742a08e0fd8f77d4699f37c22adfbfeb0c610a186b5f75e0/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7876452af029456b3f3549b696bb36a06db7c90747740c5302f74a9e9fa14b13", size = 649304 },
    { url = "https://files.pythonhosted.org/packages/f1/8e/d0aeffe69e53ccff5a28fa86f07ad1d2d2d6537a9506229431a2a02e2f15/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4ead44c85f8ab905852d3de8d86f6f8baf77109f9da589cb4fa142bd3b57b475", size = 646537 },
    { url = "https://files.pythonhosted.org/packages/05/79/e15408220bbb989469c8871062c97c6c9136770657ba779711b90870d867/greenlet-3.1.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8320f64b777d00dd7ccdade271eaf0cad6636343293a25074cc5566160e4de7b", size = 642506 },
    { url = "https://files.pythonhosted.org/packages/18/87/470e01a940307796f1d25f8167b551a968540fbe0551c0ebb853cb527dd6/greenlet-3.1.1-cp313-cp313t-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:6510bf84a6b643dabba74d3049ead221257603a253d0a9873f55f6a59a65f822", size = 602753 },
    { url = "https://files.pythonhosted.org/packages/e2/72/576815ba674eddc3c25028238f74d7b8068902b3968cbe456771b166455e/greenlet-3.1.1-cp313-cp313t-musllinux_1_1_aarch64.whl", hash = "sha256:04b013dc07c96f83134b1e99888e7a79979f1a247e2a9f59697fa14b5862ed01", size = 1122731 },
    { url = "https://files.pythonhosted.org/packages/ac/38/08cc303ddddc4b3d7c628c3039a61a3aae36c241ed01393d00c2fd663473/greenlet-3.1.1-cp313-cp313t-musllinux_1_1_x86_64.whl", hash = "sha256:411f015496fec93c1c8cd4e5238da364e1da7a124bcb293f085bf2860c32c6f6", size = 1142112 },
]

[[package]]
name = "idna"
version = "3.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f1/70/7703c29685631f5a7590aa73f1f1d3fa9a380e654b86af429e0934a32f7d/idna-3.10.tar.gz", hash = "sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9", size = 190490 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl", hash = "sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3", size = 70442 },
]

[[package]]
name = "jinja2"
version = "3.1.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/af/92/b3130cbbf5591acf9ade8708c365f3238046ac7cb8ccba6e81abccb0ccff/jinja2-3.1.5.tar.gz", hash = "sha256:8fefff8dc3034e27bb80d67c671eb8a9bc424c0ef4c0826edbff304cceff43bb", size = 244674 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bd/0f/2ba5fbcd631e3e88689309dbe978c5769e883e4b84ebfe7da30b43275c5a/jinja2-3.1.5-py3-none-any.whl", hash = "sha256:aba0f4dc9ed8013c424088f68a5c226f7d6097ed89b246d7749c2ec4175c6adb", size = 134596 },
]

[[package]]
name = "jsonschema"
version = "4.23.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "jsonschema-specifications" },
    { name = "referencing" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/2e/03362ee4034a4c917f697890ccd4aec0800ccf9ded7f511971c75451deec/jsonschema-4.23.0.tar.gz", hash = "sha256:d71497fef26351a33265337fa77ffeb82423f3ea21283cd9467bb03999266bc4", size = 325778 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/4a/4f9dbeb84e8850557c02365a0eee0649abe5eb1d84af92a25731c6c0f922/jsonschema-4.23.0-py3-none-any.whl", hash = "sha256:fbadb6f8b144a8f8cf9f0b89ba94501d143e50411a1278633f56a7acf7fd5566", size = 88462 },
]

[[package]]
name = "jsonschema-specifications"
version = "2024.10.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "referencing" },
]
sdist = { url = "https://files.pythonhosted.org/packages/10/db/58f950c996c793472e336ff3655b13fbcf1e3b359dcf52dcf3ed3b52c352/jsonschema_specifications-2024.10.1.tar.gz", hash = "sha256:0f38b83639958ce1152d02a7f062902c41c8fd20d558b0c34344292d417ae272", size = 15561 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/0f/8910b19ac0670a0f80ce1008e5e751c4a57e14d2c4c13a482aa6079fa9d6/jsonschema_specifications-2024.10.1-py3-none-any.whl", hash = "sha256:a09a0680616357d9a0ecf05c12ad234479f549239d0f5b55f3deea67475da9bf", size = 18459 },
]

[[package]]
name = "markdown-it-py"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz", hash = "sha256:e3f60a94fa066dc52ec76661e37c851cb232d92f9886b15cb560aaada2df8feb", size = 74596 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl", hash = "sha256:355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", size = 87528 },
]

[[package]]
name = "markupsafe"
version = "3.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/97/5d42485e71dfc078108a86d6de8fa46db44a1a9295e89c5d6d4a06e23a62/markupsafe-3.0.2.tar.gz", hash = "sha256:ee55d3edf80167e48ea11a923c7386f4669df67d7994554387f84e7d8b0a2bf0", size = 20537 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6b/28/bbf83e3f76936960b850435576dd5e67034e200469571be53f69174a2dfd/MarkupSafe-3.0.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:9025b4018f3a1314059769c7bf15441064b2207cb3f065e6ea1e7359cb46db9d", size = 14353 },
    { url = "https://files.pythonhosted.org/packages/6c/30/316d194b093cde57d448a4c3209f22e3046c5bb2fb0820b118292b334be7/MarkupSafe-3.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:93335ca3812df2f366e80509ae119189886b0f3c2b81325d39efdb84a1e2ae93", size = 12392 },
    { url = "https://files.pythonhosted.org/packages/f2/96/9cdafba8445d3a53cae530aaf83c38ec64c4d5427d975c974084af5bc5d2/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2cb8438c3cbb25e220c2ab33bb226559e7afb3baec11c4f218ffa7308603c832", size = 23984 },
    { url = "https://files.pythonhosted.org/packages/f1/a4/aefb044a2cd8d7334c8a47d3fb2c9f328ac48cb349468cc31c20b539305f/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a123e330ef0853c6e822384873bef7507557d8e4a082961e1defa947aa59ba84", size = 23120 },
    { url = "https://files.pythonhosted.org/packages/8d/21/5e4851379f88f3fad1de30361db501300d4f07bcad047d3cb0449fc51f8c/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1e084f686b92e5b83186b07e8a17fc09e38fff551f3602b249881fec658d3eca", size = 23032 },
    { url = "https://files.pythonhosted.org/packages/00/7b/e92c64e079b2d0d7ddf69899c98842f3f9a60a1ae72657c89ce2655c999d/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d8213e09c917a951de9d09ecee036d5c7d36cb6cb7dbaece4c71a60d79fb9798", size = 24057 },
    { url = "https://files.pythonhosted.org/packages/f9/ac/46f960ca323037caa0a10662ef97d0a4728e890334fc156b9f9e52bcc4ca/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:5b02fb34468b6aaa40dfc198d813a641e3a63b98c2b05a16b9f80b7ec314185e", size = 23359 },
    { url = "https://files.pythonhosted.org/packages/69/84/83439e16197337b8b14b6a5b9c2105fff81d42c2a7c5b58ac7b62ee2c3b1/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0bff5e0ae4ef2e1ae4fdf2dfd5b76c75e5c2fa4132d05fc1b0dabcd20c7e28c4", size = 23306 },
    { url = "https://files.pythonhosted.org/packages/9a/34/a15aa69f01e2181ed8d2b685c0d2f6655d5cca2c4db0ddea775e631918cd/MarkupSafe-3.0.2-cp311-cp311-win32.whl", hash = "sha256:6c89876f41da747c8d3677a2b540fb32ef5715f97b66eeb0c6b66f5e3ef6f59d", size = 15094 },
    { url = "https://files.pythonhosted.org/packages/da/b8/3a3bd761922d416f3dc5d00bfbed11f66b1ab89a0c2b6e887240a30b0f6b/MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:70a87b411535ccad5ef2f1df5136506a10775d267e197e4cf531ced10537bd6b", size = 15521 },
    { url = "https://files.pythonhosted.org/packages/22/09/d1f21434c97fc42f09d290cbb6350d44eb12f09cc62c9476effdb33a18aa/MarkupSafe-3.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:9778bd8ab0a994ebf6f84c2b949e65736d5575320a17ae8984a77fab08db94cf", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/6b/b0/18f76bba336fa5aecf79d45dcd6c806c280ec44538b3c13671d49099fdd0/MarkupSafe-3.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:846ade7b71e3536c4e56b386c2a47adf5741d2d8b94ec9dc3e92e5e1ee1e2225", size = 12348 },
    { url = "https://files.pythonhosted.org/packages/e0/25/dd5c0f6ac1311e9b40f4af06c78efde0f3b5cbf02502f8ef9501294c425b/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1c99d261bd2d5f6b59325c92c73df481e05e57f19837bdca8413b9eac4bd8028", size = 24149 },
    { url = "https://files.pythonhosted.org/packages/f3/f0/89e7aadfb3749d0f52234a0c8c7867877876e0a20b60e2188e9850794c17/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e17c96c14e19278594aa4841ec148115f9c7615a47382ecb6b82bd8fea3ab0c8", size = 23118 },
    { url = "https://files.pythonhosted.org/packages/d5/da/f2eeb64c723f5e3777bc081da884b414671982008c47dcc1873d81f625b6/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:88416bd1e65dcea10bc7569faacb2c20ce071dd1f87539ca2ab364bf6231393c", size = 22993 },
    { url = "https://files.pythonhosted.org/packages/da/0e/1f32af846df486dce7c227fe0f2398dc7e2e51d4a370508281f3c1c5cddc/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:2181e67807fc2fa785d0592dc2d6206c019b9502410671cc905d132a92866557", size = 24178 },
    { url = "https://files.pythonhosted.org/packages/c4/f6/bb3ca0532de8086cbff5f06d137064c8410d10779c4c127e0e47d17c0b71/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:52305740fe773d09cffb16f8ed0427942901f00adedac82ec8b67752f58a1b22", size = 23319 },
    { url = "https://files.pythonhosted.org/packages/a2/82/8be4c96ffee03c5b4a034e60a31294daf481e12c7c43ab8e34a1453ee48b/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:ad10d3ded218f1039f11a75f8091880239651b52e9bb592ca27de44eed242a48", size = 23352 },
    { url = "https://files.pythonhosted.org/packages/51/ae/97827349d3fcffee7e184bdf7f41cd6b88d9919c80f0263ba7acd1bbcb18/MarkupSafe-3.0.2-cp312-cp312-win32.whl", hash = "sha256:0f4ca02bea9a23221c0182836703cbf8930c5e9454bacce27e767509fa286a30", size = 15097 },
    { url = "https://files.pythonhosted.org/packages/c1/80/a61f99dc3a936413c3ee4e1eecac96c0da5ed07ad56fd975f1a9da5bc630/MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:8e06879fc22a25ca47312fbe7c8264eb0b662f6db27cb2d3bbbc74b1df4b9b87", size = 15601 },
    { url = "https://files.pythonhosted.org/packages/83/0e/67eb10a7ecc77a0c2bbe2b0235765b98d164d81600746914bebada795e97/MarkupSafe-3.0.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:ba9527cdd4c926ed0760bc301f6728ef34d841f405abf9d4f959c478421e4efd", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/2b/6d/9409f3684d3335375d04e5f05744dfe7e9f120062c9857df4ab490a1031a/MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f8b3d067f2e40fe93e1ccdd6b2e1d16c43140e76f02fb1319a05cf2b79d99430", size = 12352 },
    { url = "https://files.pythonhosted.org/packages/d2/f5/6eadfcd3885ea85fe2a7c128315cc1bb7241e1987443d78c8fe712d03091/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:569511d3b58c8791ab4c2e1285575265991e6d8f8700c7be0e88f86cb0672094", size = 24122 },
    { url = "https://files.pythonhosted.org/packages/0c/91/96cf928db8236f1bfab6ce15ad070dfdd02ed88261c2afafd4b43575e9e9/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:15ab75ef81add55874e7ab7055e9c397312385bd9ced94920f2802310c930396", size = 23085 },
    { url = "https://files.pythonhosted.org/packages/c2/cf/c9d56af24d56ea04daae7ac0940232d31d5a8354f2b457c6d856b2057d69/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f3818cb119498c0678015754eba762e0d61e5b52d34c8b13d770f0719f7b1d79", size = 22978 },
    { url = "https://files.pythonhosted.org/packages/2a/9f/8619835cd6a711d6272d62abb78c033bda638fdc54c4e7f4272cf1c0962b/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:cdb82a876c47801bb54a690c5ae105a46b392ac6099881cdfb9f6e95e4014c6a", size = 24208 },
    { url = "https://files.pythonhosted.org/packages/f9/bf/176950a1792b2cd2102b8ffeb5133e1ed984547b75db47c25a67d3359f77/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:cabc348d87e913db6ab4aa100f01b08f481097838bdddf7c7a84b7575b7309ca", size = 23357 },
    { url = "https://files.pythonhosted.org/packages/ce/4f/9a02c1d335caabe5c4efb90e1b6e8ee944aa245c1aaaab8e8a618987d816/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:444dcda765c8a838eaae23112db52f1efaf750daddb2d9ca300bcae1039adc5c", size = 23344 },
    { url = "https://files.pythonhosted.org/packages/ee/55/c271b57db36f748f0e04a759ace9f8f759ccf22b4960c270c78a394f58be/MarkupSafe-3.0.2-cp313-cp313-win32.whl", hash = "sha256:bcf3e58998965654fdaff38e58584d8937aa3096ab5354d493c77d1fdd66d7a1", size = 15101 },
    { url = "https://files.pythonhosted.org/packages/29/88/07df22d2dd4df40aba9f3e402e6dc1b8ee86297dddbad4872bd5e7b0094f/MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:e6a2a455bd412959b57a172ce6328d2dd1f01cb2135efda2e4576e8a23fa3b0f", size = 15603 },
    { url = "https://files.pythonhosted.org/packages/62/6a/8b89d24db2d32d433dffcd6a8779159da109842434f1dd2f6e71f32f738c/MarkupSafe-3.0.2-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:b5a6b3ada725cea8a5e634536b1b01c30bcdcd7f9c6fff4151548d5bf6b3a36c", size = 14510 },
    { url = "https://files.pythonhosted.org/packages/7a/06/a10f955f70a2e5a9bf78d11a161029d278eeacbd35ef806c3fd17b13060d/MarkupSafe-3.0.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:a904af0a6162c73e3edcb969eeeb53a63ceeb5d8cf642fade7d39e7963a22ddb", size = 12486 },
    { url = "https://files.pythonhosted.org/packages/34/cf/65d4a571869a1a9078198ca28f39fba5fbb910f952f9dbc5220afff9f5e6/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4aa4e5faecf353ed117801a068ebab7b7e09ffb6e1d5e412dc852e0da018126c", size = 25480 },
    { url = "https://files.pythonhosted.org/packages/0c/e3/90e9651924c430b885468b56b3d597cabf6d72be4b24a0acd1fa0e12af67/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c0ef13eaeee5b615fb07c9a7dadb38eac06a0608b41570d8ade51c56539e509d", size = 23914 },
    { url = "https://files.pythonhosted.org/packages/66/8c/6c7cf61f95d63bb866db39085150df1f2a5bd3335298f14a66b48e92659c/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d16a81a06776313e817c951135cf7340a3e91e8c1ff2fac444cfd75fffa04afe", size = 23796 },
    { url = "https://files.pythonhosted.org/packages/bb/35/cbe9238ec3f47ac9a7c8b3df7a808e7cb50fe149dc7039f5f454b3fba218/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:6381026f158fdb7c72a168278597a5e3a5222e83ea18f543112b2662a9b699c5", size = 25473 },
    { url = "https://files.pythonhosted.org/packages/e6/32/7621a4382488aa283cc05e8984a9c219abad3bca087be9ec77e89939ded9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:3d79d162e7be8f996986c064d1c7c817f6df3a77fe3d6859f6f9e7be4b8c213a", size = 24114 },
    { url = "https://files.pythonhosted.org/packages/0d/80/0985960e4b89922cb5a0bac0ed39c5b96cbc1a536a99f30e8c220a996ed9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:131a3c7689c85f5ad20f9f6fb1b866f402c445b220c19fe4308c0b147ccd2ad9", size = 24098 },
    { url = "https://files.pythonhosted.org/packages/82/78/fedb03c7d5380df2427038ec8d973587e90561b2d90cd472ce9254cf348b/MarkupSafe-3.0.2-cp313-cp313t-win32.whl", hash = "sha256:ba8062ed2cf21c07a9e295d5b8a2a5ce678b913b45fdf68c32d95d6c1291e0b6", size = 15208 },
    { url = "https://files.pythonhosted.org/packages/4f/65/6079a46068dfceaeabb5dcad6d674f5f5c61a6fa5673746f42a9f4c233b3/MarkupSafe-3.0.2-cp313-cp313t-win_amd64.whl", hash = "sha256:e444a31f8db13eb18ada366ab3cf45fd4b31e4db1236a4448f68778c1d1a5a2f", size = 15739 },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979 },
]

[[package]]
name = "narwhals"
version = "1.28.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ba/65/cc4f1d02d418e587fc5b9b31f3cbb8db83f4b35f91d7b59adfa8d947f644/narwhals-1.28.0.tar.gz", hash = "sha256:a2213fa44a039f724278fb15609889319e7c240403413f2606cc856c8d8f708d", size = 252143 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/73/aa/eedf2ade0c16a60541ca7acd48665c62dc0d11e1e910467b6c7e6b1eda34/narwhals-1.28.0-py3-none-any.whl", hash = "sha256:45d909ad6240944d447b0dae38074c5a919830dff3868d57b05a5526c1f06fe4", size = 308950 },
]

[[package]]
name = "numpy"
version = "2.2.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fb/90/8956572f5c4ae52201fdec7ba2044b2c882832dcec7d5d0922c9e9acf2de/numpy-2.2.3.tar.gz", hash = "sha256:dbdc15f0c81611925f382dfa97b3bd0bc2c1ce19d4fe50482cb0ddc12ba30020", size = 20262700 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/96/86/453aa3949eab6ff54e2405f9cb0c01f756f031c3dc2a6d60a1d40cba5488/numpy-2.2.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:16372619ee728ed67a2a606a614f56d3eabc5b86f8b615c79d01957062826ca8", size = 21237256 },
    { url = "https://files.pythonhosted.org/packages/20/c3/93ecceadf3e155d6a9e4464dd2392d8d80cf436084c714dc8535121c83e8/numpy-2.2.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:5521a06a3148686d9269c53b09f7d399a5725c47bbb5b35747e1cb76326b714b", size = 14408049 },
    { url = "https://files.pythonhosted.org/packages/8d/29/076999b69bd9264b8df5e56f2be18da2de6b2a2d0e10737e5307592e01de/numpy-2.2.3-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:7c8dde0ca2f77828815fd1aedfdf52e59071a5bae30dac3b4da2a335c672149a", size = 5408655 },
    { url = "https://files.pythonhosted.org/packages/e2/a7/b14f0a73eb0fe77cb9bd5b44534c183b23d4229c099e339c522724b02678/numpy-2.2.3-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:77974aba6c1bc26e3c205c2214f0d5b4305bdc719268b93e768ddb17e3fdd636", size = 6949996 },
    { url = "https://files.pythonhosted.org/packages/72/2f/8063da0616bb0f414b66dccead503bd96e33e43685c820e78a61a214c098/numpy-2.2.3-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d42f9c36d06440e34226e8bd65ff065ca0963aeecada587b937011efa02cdc9d", size = 14355789 },
    { url = "https://files.pythonhosted.org/packages/e6/d7/3cd47b00b8ea95ab358c376cf5602ad21871410950bc754cf3284771f8b6/numpy-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f2712c5179f40af9ddc8f6727f2bd910ea0eb50206daea75f58ddd9fa3f715bb", size = 16411356 },
    { url = "https://files.pythonhosted.org/packages/27/c0/a2379e202acbb70b85b41483a422c1e697ff7eee74db642ca478de4ba89f/numpy-2.2.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c8b0451d2ec95010d1db8ca733afc41f659f425b7f608af569711097fd6014e2", size = 15576770 },
    { url = "https://files.pythonhosted.org/packages/bc/63/a13ee650f27b7999e5b9e1964ae942af50bb25606d088df4229283eda779/numpy-2.2.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:d9b4a8148c57ecac25a16b0e11798cbe88edf5237b0df99973687dd866f05e1b", size = 18200483 },
    { url = "https://files.pythonhosted.org/packages/4c/87/e71f89935e09e8161ac9c590c82f66d2321eb163893a94af749dfa8a3cf8/numpy-2.2.3-cp311-cp311-win32.whl", hash = "sha256:1f45315b2dc58d8a3e7754fe4e38b6fce132dab284a92851e41b2b344f6441c5", size = 6588415 },
    { url = "https://files.pythonhosted.org/packages/b9/c6/cd4298729826af9979c5f9ab02fcaa344b82621e7c49322cd2d210483d3f/numpy-2.2.3-cp311-cp311-win_amd64.whl", hash = "sha256:9f48ba6f6c13e5e49f3d3efb1b51c8193215c42ac82610a04624906a9270be6f", size = 12929604 },
    { url = "https://files.pythonhosted.org/packages/43/ec/43628dcf98466e087812142eec6d1c1a6c6bdfdad30a0aa07b872dc01f6f/numpy-2.2.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:12c045f43b1d2915eca6b880a7f4a256f59d62df4f044788c8ba67709412128d", size = 20929458 },
    { url = "https://files.pythonhosted.org/packages/9b/c0/2f4225073e99a5c12350954949ed19b5d4a738f541d33e6f7439e33e98e4/numpy-2.2.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:87eed225fd415bbae787f93a457af7f5990b92a334e346f72070bf569b9c9c95", size = 14115299 },
    { url = "https://files.pythonhosted.org/packages/ca/fa/d2c5575d9c734a7376cc1592fae50257ec95d061b27ee3dbdb0b3b551eb2/numpy-2.2.3-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:712a64103d97c404e87d4d7c47fb0c7ff9acccc625ca2002848e0d53288b90ea", size = 5145723 },
    { url = "https://files.pythonhosted.org/packages/eb/dc/023dad5b268a7895e58e791f28dc1c60eb7b6c06fcbc2af8538ad069d5f3/numpy-2.2.3-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:a5ae282abe60a2db0fd407072aff4599c279bcd6e9a2475500fc35b00a57c532", size = 6678797 },
    { url = "https://files.pythonhosted.org/packages/3f/19/bcd641ccf19ac25abb6fb1dcd7744840c11f9d62519d7057b6ab2096eb60/numpy-2.2.3-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5266de33d4c3420973cf9ae3b98b54a2a6d53a559310e3236c4b2b06b9c07d4e", size = 14067362 },
    { url = "https://files.pythonhosted.org/packages/39/04/78d2e7402fb479d893953fb78fa7045f7deb635ec095b6b4f0260223091a/numpy-2.2.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3b787adbf04b0db1967798dba8da1af07e387908ed1553a0d6e74c084d1ceafe", size = 16116679 },
    { url = "https://files.pythonhosted.org/packages/d0/a1/e90f7aa66512be3150cb9d27f3d9995db330ad1b2046474a13b7040dfd92/numpy-2.2.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:34c1b7e83f94f3b564b35f480f5652a47007dd91f7c839f404d03279cc8dd021", size = 15264272 },
    { url = "https://files.pythonhosted.org/packages/dc/b6/50bd027cca494de4fa1fc7bf1662983d0ba5f256fa0ece2c376b5eb9b3f0/numpy-2.2.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:4d8335b5f1b6e2bce120d55fb17064b0262ff29b459e8493d1785c18ae2553b8", size = 17880549 },
    { url = "https://files.pythonhosted.org/packages/96/30/f7bf4acb5f8db10a96f73896bdeed7a63373137b131ca18bd3dab889db3b/numpy-2.2.3-cp312-cp312-win32.whl", hash = "sha256:4d9828d25fb246bedd31e04c9e75714a4087211ac348cb39c8c5f99dbb6683fe", size = 6293394 },
    { url = "https://files.pythonhosted.org/packages/42/6e/55580a538116d16ae7c9aa17d4edd56e83f42126cb1dfe7a684da7925d2c/numpy-2.2.3-cp312-cp312-win_amd64.whl", hash = "sha256:83807d445817326b4bcdaaaf8e8e9f1753da04341eceec705c001ff342002e5d", size = 12626357 },
    { url = "https://files.pythonhosted.org/packages/0e/8b/88b98ed534d6a03ba8cddb316950fe80842885709b58501233c29dfa24a9/numpy-2.2.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:7bfdb06b395385ea9b91bf55c1adf1b297c9fdb531552845ff1d3ea6e40d5aba", size = 20916001 },
    { url = "https://files.pythonhosted.org/packages/d9/b4/def6ec32c725cc5fbd8bdf8af80f616acf075fe752d8a23e895da8c67b70/numpy-2.2.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:23c9f4edbf4c065fddb10a4f6e8b6a244342d95966a48820c614891e5059bb50", size = 14130721 },
    { url = "https://files.pythonhosted.org/packages/20/60/70af0acc86495b25b672d403e12cb25448d79a2b9658f4fc45e845c397a8/numpy-2.2.3-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:a0c03b6be48aaf92525cccf393265e02773be8fd9551a2f9adbe7db1fa2b60f1", size = 5130999 },
    { url = "https://files.pythonhosted.org/packages/2e/69/d96c006fb73c9a47bcb3611417cf178049aae159afae47c48bd66df9c536/numpy-2.2.3-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:2376e317111daa0a6739e50f7ee2a6353f768489102308b0d98fcf4a04f7f3b5", size = 6665299 },
    { url = "https://files.pythonhosted.org/packages/5a/3f/d8a877b6e48103733ac224ffa26b30887dc9944ff95dffdfa6c4ce3d7df3/numpy-2.2.3-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8fb62fe3d206d72fe1cfe31c4a1106ad2b136fcc1606093aeab314f02930fdf2", size = 14064096 },
    { url = "https://files.pythonhosted.org/packages/e4/43/619c2c7a0665aafc80efca465ddb1f260287266bdbdce517396f2f145d49/numpy-2.2.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:52659ad2534427dffcc36aac76bebdd02b67e3b7a619ac67543bc9bfe6b7cdb1", size = 16114758 },
    { url = "https://files.pythonhosted.org/packages/d9/79/ee4fe4f60967ccd3897aa71ae14cdee9e3c097e3256975cc9575d393cb42/numpy-2.2.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:1b416af7d0ed3271cad0f0a0d0bee0911ed7eba23e66f8424d9f3dfcdcae1304", size = 15259880 },
    { url = "https://files.pythonhosted.org/packages/fb/c8/8b55cf05db6d85b7a7d414b3d1bd5a740706df00bfa0824a08bf041e52ee/numpy-2.2.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:1402da8e0f435991983d0a9708b779f95a8c98c6b18a171b9f1be09005e64d9d", size = 17876721 },
    { url = "https://files.pythonhosted.org/packages/21/d6/b4c2f0564b7dcc413117b0ffbb818d837e4b29996b9234e38b2025ed24e7/numpy-2.2.3-cp313-cp313-win32.whl", hash = "sha256:136553f123ee2951bfcfbc264acd34a2fc2f29d7cdf610ce7daf672b6fbaa693", size = 6290195 },
    { url = "https://files.pythonhosted.org/packages/97/e7/7d55a86719d0de7a6a597949f3febefb1009435b79ba510ff32f05a8c1d7/numpy-2.2.3-cp313-cp313-win_amd64.whl", hash = "sha256:5b732c8beef1d7bc2d9e476dbba20aaff6167bf205ad9aa8d30913859e82884b", size = 12619013 },
    { url = "https://files.pythonhosted.org/packages/a6/1f/0b863d5528b9048fd486a56e0b97c18bf705e88736c8cea7239012119a54/numpy-2.2.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:435e7a933b9fda8126130b046975a968cc2d833b505475e588339e09f7672890", size = 20944621 },
    { url = "https://files.pythonhosted.org/packages/aa/99/b478c384f7a0a2e0736177aafc97dc9152fc036a3fdb13f5a3ab225f1494/numpy-2.2.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:7678556eeb0152cbd1522b684dcd215250885993dd00adb93679ec3c0e6e091c", size = 14142502 },
    { url = "https://files.pythonhosted.org/packages/fb/61/2d9a694a0f9cd0a839501d362de2a18de75e3004576a3008e56bdd60fcdb/numpy-2.2.3-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:2e8da03bd561504d9b20e7a12340870dfc206c64ea59b4cfee9fceb95070ee94", size = 5176293 },
    { url = "https://files.pythonhosted.org/packages/33/35/51e94011b23e753fa33f891f601e5c1c9a3d515448659b06df9d40c0aa6e/numpy-2.2.3-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:c9aa4496fd0e17e3843399f533d62857cef5900facf93e735ef65aa4bbc90ef0", size = 6691874 },
    { url = "https://files.pythonhosted.org/packages/ff/cf/06e37619aad98a9d03bd8d65b8e3041c3a639be0f5f6b0a0e2da544538d4/numpy-2.2.3-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f4ca91d61a4bf61b0f2228f24bbfa6a9facd5f8af03759fe2a655c50ae2c6610", size = 14036826 },
    { url = "https://files.pythonhosted.org/packages/0c/93/5d7d19955abd4d6099ef4a8ee006f9ce258166c38af259f9e5558a172e3e/numpy-2.2.3-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:deaa09cd492e24fd9b15296844c0ad1b3c976da7907e1c1ed3a0ad21dded6f76", size = 16096567 },
    { url = "https://files.pythonhosted.org/packages/af/53/d1c599acf7732d81f46a93621dab6aa8daad914b502a7a115b3f17288ab2/numpy-2.2.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:246535e2f7496b7ac85deffe932896a3577be7af8fb7eebe7146444680297e9a", size = 15242514 },
    { url = "https://files.pythonhosted.org/packages/53/43/c0f5411c7b3ea90adf341d05ace762dad8cb9819ef26093e27b15dd121ac/numpy-2.2.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:daf43a3d1ea699402c5a850e5313680ac355b4adc9770cd5cfc2940e7861f1bf", size = 17872920 },
    { url = "https://files.pythonhosted.org/packages/5b/57/6dbdd45ab277aff62021cafa1e15f9644a52f5b5fc840bc7591b4079fb58/numpy-2.2.3-cp313-cp313t-win32.whl", hash = "sha256:cf802eef1f0134afb81fef94020351be4fe1d6681aadf9c5e862af6602af64ef", size = 6346584 },
    { url = "https://files.pythonhosted.org/packages/97/9b/484f7d04b537d0a1202a5ba81c6f53f1846ae6c63c2127f8df869ed31342/numpy-2.2.3-cp313-cp313t-win_amd64.whl", hash = "sha256:aee2512827ceb6d7f517c8b85aa5d3923afe8fc7a57d028cffcd522f1c6fd082", size = 12706784 },
]

[[package]]
name = "packaging"
version = "24.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d0/63/68dbb6eb2de9cb10ee4c9c14a0148804425e13c4fb20d61cce69f53106da/packaging-24.2.tar.gz", hash = "sha256:c228a6dc5e932d346bc5739379109d49e8853dd8223571c7c5b55260edc0b97f", size = 163950 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl", hash = "sha256:09abb1bccd265c01f4a3aa3f7a7db064b36514d2cba19a2f694fe6150451a759", size = 65451 },
]

[[package]]
name = "pandas"
version = "2.2.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "numpy" },
    { name = "python-dateutil" },
    { name = "pytz" },
    { name = "tzdata" },
]
sdist = { url = "https://files.pythonhosted.org/packages/9c/d6/9f8431bacc2e19dca897724cd097b1bb224a6ad5433784a44b587c7c13af/pandas-2.2.3.tar.gz", hash = "sha256:4f18ba62b61d7e192368b84517265a99b4d7ee8912f8708660fb4a366cc82667", size = 4399213 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a8/44/d9502bf0ed197ba9bf1103c9867d5904ddcaf869e52329787fc54ed70cc8/pandas-2.2.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:66108071e1b935240e74525006034333f98bcdb87ea116de573a6a0dccb6c039", size = 12602222 },
    { url = "https://files.pythonhosted.org/packages/52/11/9eac327a38834f162b8250aab32a6781339c69afe7574368fffe46387edf/pandas-2.2.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7c2875855b0ff77b2a64a0365e24455d9990730d6431b9e0ee18ad8acee13dbd", size = 11321274 },
    { url = "https://files.pythonhosted.org/packages/45/fb/c4beeb084718598ba19aa9f5abbc8aed8b42f90930da861fcb1acdb54c3a/pandas-2.2.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:cd8d0c3be0515c12fed0bdbae072551c8b54b7192c7b1fda0ba56059a0179698", size = 15579836 },
    { url = "https://files.pythonhosted.org/packages/cd/5f/4dba1d39bb9c38d574a9a22548c540177f78ea47b32f99c0ff2ec499fac5/pandas-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c124333816c3a9b03fbeef3a9f230ba9a737e9e5bb4060aa2107a86cc0a497fc", size = 13058505 },
    { url = "https://files.pythonhosted.org/packages/b9/57/708135b90391995361636634df1f1130d03ba456e95bcf576fada459115a/pandas-2.2.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:63cc132e40a2e084cf01adf0775b15ac515ba905d7dcca47e9a251819c575ef3", size = 16744420 },
    { url = "https://files.pythonhosted.org/packages/86/4a/03ed6b7ee323cf30404265c284cee9c65c56a212e0a08d9ee06984ba2240/pandas-2.2.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:29401dbfa9ad77319367d36940cd8a0b3a11aba16063e39632d98b0e931ddf32", size = 14440457 },
    { url = "https://files.pythonhosted.org/packages/ed/8c/87ddf1fcb55d11f9f847e3c69bb1c6f8e46e2f40ab1a2d2abadb2401b007/pandas-2.2.3-cp311-cp311-win_amd64.whl", hash = "sha256:3fc6873a41186404dad67245896a6e440baacc92f5b716ccd1bc9ed2995ab2c5", size = 11617166 },
    { url = "https://files.pythonhosted.org/packages/17/a3/fb2734118db0af37ea7433f57f722c0a56687e14b14690edff0cdb4b7e58/pandas-2.2.3-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:b1d432e8d08679a40e2a6d8b2f9770a5c21793a6f9f47fdd52c5ce1948a5a8a9", size = 12529893 },
    { url = "https://files.pythonhosted.org/packages/e1/0c/ad295fd74bfac85358fd579e271cded3ac969de81f62dd0142c426b9da91/pandas-2.2.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a5a1595fe639f5988ba6a8e5bc9649af3baf26df3998a0abe56c02609392e0a4", size = 11363475 },
    { url = "https://files.pythonhosted.org/packages/c6/2a/4bba3f03f7d07207481fed47f5b35f556c7441acddc368ec43d6643c5777/pandas-2.2.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:5de54125a92bb4d1c051c0659e6fcb75256bf799a732a87184e5ea503965bce3", size = 15188645 },
    { url = "https://files.pythonhosted.org/packages/38/f8/d8fddee9ed0d0c0f4a2132c1dfcf0e3e53265055da8df952a53e7eaf178c/pandas-2.2.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fffb8ae78d8af97f849404f21411c95062db1496aeb3e56f146f0355c9989319", size = 12739445 },
    { url = "https://files.pythonhosted.org/packages/20/e8/45a05d9c39d2cea61ab175dbe6a2de1d05b679e8de2011da4ee190d7e748/pandas-2.2.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6dfcb5ee8d4d50c06a51c2fffa6cff6272098ad6540aed1a76d15fb9318194d8", size = 16359235 },
    { url = "https://files.pythonhosted.org/packages/1d/99/617d07a6a5e429ff90c90da64d428516605a1ec7d7bea494235e1c3882de/pandas-2.2.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:062309c1b9ea12a50e8ce661145c6aab431b1e99530d3cd60640e255778bd43a", size = 14056756 },
    { url = "https://files.pythonhosted.org/packages/29/d4/1244ab8edf173a10fd601f7e13b9566c1b525c4f365d6bee918e68381889/pandas-2.2.3-cp312-cp312-win_amd64.whl", hash = "sha256:59ef3764d0fe818125a5097d2ae867ca3fa64df032331b7e0917cf5d7bf66b13", size = 11504248 },
    { url = "https://files.pythonhosted.org/packages/64/22/3b8f4e0ed70644e85cfdcd57454686b9057c6c38d2f74fe4b8bc2527214a/pandas-2.2.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f00d1345d84d8c86a63e476bb4955e46458b304b9575dcf71102b5c705320015", size = 12477643 },
    { url = "https://files.pythonhosted.org/packages/e4/93/b3f5d1838500e22c8d793625da672f3eec046b1a99257666c94446969282/pandas-2.2.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:3508d914817e153ad359d7e069d752cdd736a247c322d932eb89e6bc84217f28", size = 11281573 },
    { url = "https://files.pythonhosted.org/packages/f5/94/6c79b07f0e5aab1dcfa35a75f4817f5c4f677931d4234afcd75f0e6a66ca/pandas-2.2.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:22a9d949bfc9a502d320aa04e5d02feab689d61da4e7764b62c30b991c42c5f0", size = 15196085 },
    { url = "https://files.pythonhosted.org/packages/e8/31/aa8da88ca0eadbabd0a639788a6da13bb2ff6edbbb9f29aa786450a30a91/pandas-2.2.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f3a255b2c19987fbbe62a9dfd6cff7ff2aa9ccab3fc75218fd4b7530f01efa24", size = 12711809 },
    { url = "https://files.pythonhosted.org/packages/ee/7c/c6dbdb0cb2a4344cacfb8de1c5808ca885b2e4dcfde8008266608f9372af/pandas-2.2.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:800250ecdadb6d9c78eae4990da62743b857b470883fa27f652db8bdde7f6659", size = 16356316 },
    { url = "https://files.pythonhosted.org/packages/57/b7/8b757e7d92023b832869fa8881a992696a0bfe2e26f72c9ae9f255988d42/pandas-2.2.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6374c452ff3ec675a8f46fd9ab25c4ad0ba590b71cf0656f8b6daa5202bca3fb", size = 14022055 },
    { url = "https://files.pythonhosted.org/packages/3b/bc/4b18e2b8c002572c5a441a64826252ce5da2aa738855747247a971988043/pandas-2.2.3-cp313-cp313-win_amd64.whl", hash = "sha256:61c5ad4043f791b61dd4752191d9f07f0ae412515d59ba8f005832a532f8736d", size = 11481175 },
    { url = "https://files.pythonhosted.org/packages/76/a3/a5d88146815e972d40d19247b2c162e88213ef51c7c25993942c39dbf41d/pandas-2.2.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:3b71f27954685ee685317063bf13c7709a7ba74fc996b84fc6821c59b0f06468", size = 12615650 },
    { url = "https://files.pythonhosted.org/packages/9c/8c/f0fd18f6140ddafc0c24122c8a964e48294acc579d47def376fef12bcb4a/pandas-2.2.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:38cf8125c40dae9d5acc10fa66af8ea6fdf760b2714ee482ca691fc66e6fcb18", size = 11290177 },
    { url = "https://files.pythonhosted.org/packages/ed/f9/e995754eab9c0f14c6777401f7eece0943840b7a9fc932221c19d1abee9f/pandas-2.2.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:ba96630bc17c875161df3818780af30e43be9b166ce51c9a18c1feae342906c2", size = 14651526 },
    { url = "https://files.pythonhosted.org/packages/25/b0/98d6ae2e1abac4f35230aa756005e8654649d305df9a28b16b9ae4353bff/pandas-2.2.3-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1db71525a1538b30142094edb9adc10be3f3e176748cd7acc2240c2f2e5aa3a4", size = 11871013 },
    { url = "https://files.pythonhosted.org/packages/cc/57/0f72a10f9db6a4628744c8e8f0df4e6e21de01212c7c981d31e50ffc8328/pandas-2.2.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:15c0e1e02e93116177d29ff83e8b1619c93ddc9c49083f237d4312337a61165d", size = 15711620 },
    { url = "https://files.pythonhosted.org/packages/ab/5f/b38085618b950b79d2d9164a711c52b10aefc0ae6833b96f626b7021b2ed/pandas-2.2.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:ad5b65698ab28ed8d7f18790a0dc58005c7629f227be9ecc1072aa74c0c1d43a", size = 13098436 },
]

[[package]]
name = "pillow"
version = "11.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/af/c097e544e7bd278333db77933e535098c259609c4eb3b85381109602fb5b/pillow-11.1.0.tar.gz", hash = "sha256:368da70808b36d73b4b390a8ffac11069f8a5c85f29eff1f1b01bcf3ef5b2a20", size = 46742715 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dd/d6/2000bfd8d5414fb70cbbe52c8332f2283ff30ed66a9cde42716c8ecbe22c/pillow-11.1.0-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:e06695e0326d05b06833b40b7ef477e475d0b1ba3a6d27da1bb48c23209bf457", size = 3229968 },
    { url = "https://files.pythonhosted.org/packages/d9/45/3fe487010dd9ce0a06adf9b8ff4f273cc0a44536e234b0fad3532a42c15b/pillow-11.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:96f82000e12f23e4f29346e42702b6ed9a2f2fea34a740dd5ffffcc8c539eb35", size = 3101806 },
    { url = "https://files.pythonhosted.org/packages/e3/72/776b3629c47d9d5f1c160113158a7a7ad177688d3a1159cd3b62ded5a33a/pillow-11.1.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a3cd561ded2cf2bbae44d4605837221b987c216cff94f49dfeed63488bb228d2", size = 4322283 },
    { url = "https://files.pythonhosted.org/packages/e4/c2/e25199e7e4e71d64eeb869f5b72c7ddec70e0a87926398785ab944d92375/pillow-11.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f189805c8be5ca5add39e6f899e6ce2ed824e65fb45f3c28cb2841911da19070", size = 4402945 },
    { url = "https://files.pythonhosted.org/packages/c1/ed/51d6136c9d5911f78632b1b86c45241c712c5a80ed7fa7f9120a5dff1eba/pillow-11.1.0-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:dd0052e9db3474df30433f83a71b9b23bd9e4ef1de13d92df21a52c0303b8ab6", size = 4361228 },
    { url = "https://files.pythonhosted.org/packages/48/a4/fbfe9d5581d7b111b28f1d8c2762dee92e9821bb209af9fa83c940e507a0/pillow-11.1.0-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:837060a8599b8f5d402e97197d4924f05a2e0d68756998345c829c33186217b1", size = 4484021 },
    { url = "https://files.pythonhosted.org/packages/39/db/0b3c1a5018117f3c1d4df671fb8e47d08937f27519e8614bbe86153b65a5/pillow-11.1.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:aa8dd43daa836b9a8128dbe7d923423e5ad86f50a7a14dc688194b7be5c0dea2", size = 4287449 },
    { url = "https://files.pythonhosted.org/packages/d9/58/bc128da7fea8c89fc85e09f773c4901e95b5936000e6f303222490c052f3/pillow-11.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0a2f91f8a8b367e7a57c6e91cd25af510168091fb89ec5146003e424e1558a96", size = 4419972 },
    { url = "https://files.pythonhosted.org/packages/5f/bb/58f34379bde9fe197f51841c5bbe8830c28bbb6d3801f16a83b8f2ad37df/pillow-11.1.0-cp311-cp311-win32.whl", hash = "sha256:c12fc111ef090845de2bb15009372175d76ac99969bdf31e2ce9b42e4b8cd88f", size = 2291201 },
    { url = "https://files.pythonhosted.org/packages/3a/c6/fce9255272bcf0c39e15abd2f8fd8429a954cf344469eaceb9d0d1366913/pillow-11.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:fbd43429d0d7ed6533b25fc993861b8fd512c42d04514a0dd6337fb3ccf22761", size = 2625686 },
    { url = "https://files.pythonhosted.org/packages/c8/52/8ba066d569d932365509054859f74f2a9abee273edcef5cd75e4bc3e831e/pillow-11.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:f7955ecf5609dee9442cbface754f2c6e541d9e6eda87fad7f7a989b0bdb9d71", size = 2375194 },
    { url = "https://files.pythonhosted.org/packages/95/20/9ce6ed62c91c073fcaa23d216e68289e19d95fb8188b9fb7a63d36771db8/pillow-11.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:2062ffb1d36544d42fcaa277b069c88b01bb7298f4efa06731a7fd6cc290b81a", size = 3226818 },
    { url = "https://files.pythonhosted.org/packages/b9/d8/f6004d98579a2596c098d1e30d10b248798cceff82d2b77aa914875bfea1/pillow-11.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a85b653980faad27e88b141348707ceeef8a1186f75ecc600c395dcac19f385b", size = 3101662 },
    { url = "https://files.pythonhosted.org/packages/08/d9/892e705f90051c7a2574d9f24579c9e100c828700d78a63239676f960b74/pillow-11.1.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9409c080586d1f683df3f184f20e36fb647f2e0bc3988094d4fd8c9f4eb1b3b3", size = 4329317 },
    { url = "https://files.pythonhosted.org/packages/8c/aa/7f29711f26680eab0bcd3ecdd6d23ed6bce180d82e3f6380fb7ae35fcf3b/pillow-11.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7fdadc077553621911f27ce206ffcbec7d3f8d7b50e0da39f10997e8e2bb7f6a", size = 4412999 },
    { url = "https://files.pythonhosted.org/packages/c8/c4/8f0fe3b9e0f7196f6d0bbb151f9fba323d72a41da068610c4c960b16632a/pillow-11.1.0-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:93a18841d09bcdd774dcdc308e4537e1f867b3dec059c131fde0327899734aa1", size = 4368819 },
    { url = "https://files.pythonhosted.org/packages/38/0d/84200ed6a871ce386ddc82904bfadc0c6b28b0c0ec78176871a4679e40b3/pillow-11.1.0-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:9aa9aeddeed452b2f616ff5507459e7bab436916ccb10961c4a382cd3e03f47f", size = 4496081 },
    { url = "https://files.pythonhosted.org/packages/84/9c/9bcd66f714d7e25b64118e3952d52841a4babc6d97b6d28e2261c52045d4/pillow-11.1.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:3cdcdb0b896e981678eee140d882b70092dac83ac1cdf6b3a60e2216a73f2b91", size = 4296513 },
    { url = "https://files.pythonhosted.org/packages/db/61/ada2a226e22da011b45f7104c95ebda1b63dcbb0c378ad0f7c2a710f8fd2/pillow-11.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:36ba10b9cb413e7c7dfa3e189aba252deee0602c86c309799da5a74009ac7a1c", size = 4431298 },
    { url = "https://files.pythonhosted.org/packages/e7/c4/fc6e86750523f367923522014b821c11ebc5ad402e659d8c9d09b3c9d70c/pillow-11.1.0-cp312-cp312-win32.whl", hash = "sha256:cfd5cd998c2e36a862d0e27b2df63237e67273f2fc78f47445b14e73a810e7e6", size = 2291630 },
    { url = "https://files.pythonhosted.org/packages/08/5c/2104299949b9d504baf3f4d35f73dbd14ef31bbd1ddc2c1b66a5b7dfda44/pillow-11.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:a697cd8ba0383bba3d2d3ada02b34ed268cb548b369943cd349007730c92bddf", size = 2626369 },
    { url = "https://files.pythonhosted.org/packages/37/f3/9b18362206b244167c958984b57c7f70a0289bfb59a530dd8af5f699b910/pillow-11.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:4dd43a78897793f60766563969442020e90eb7847463eca901e41ba186a7d4a5", size = 2375240 },
    { url = "https://files.pythonhosted.org/packages/b3/31/9ca79cafdce364fd5c980cd3416c20ce1bebd235b470d262f9d24d810184/pillow-11.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ae98e14432d458fc3de11a77ccb3ae65ddce70f730e7c76140653048c71bfcbc", size = 3226640 },
    { url = "https://files.pythonhosted.org/packages/ac/0f/ff07ad45a1f172a497aa393b13a9d81a32e1477ef0e869d030e3c1532521/pillow-11.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:cc1331b6d5a6e144aeb5e626f4375f5b7ae9934ba620c0ac6b3e43d5e683a0f0", size = 3101437 },
    { url = "https://files.pythonhosted.org/packages/08/2f/9906fca87a68d29ec4530be1f893149e0cb64a86d1f9f70a7cfcdfe8ae44/pillow-11.1.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:758e9d4ef15d3560214cddbc97b8ef3ef86ce04d62ddac17ad39ba87e89bd3b1", size = 4326605 },
    { url = "https://files.pythonhosted.org/packages/b0/0f/f3547ee15b145bc5c8b336401b2d4c9d9da67da9dcb572d7c0d4103d2c69/pillow-11.1.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b523466b1a31d0dcef7c5be1f20b942919b62fd6e9a9be199d035509cbefc0ec", size = 4411173 },
    { url = "https://files.pythonhosted.org/packages/b1/df/bf8176aa5db515c5de584c5e00df9bab0713548fd780c82a86cba2c2fedb/pillow-11.1.0-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:9044b5e4f7083f209c4e35aa5dd54b1dd5b112b108648f5c902ad586d4f945c5", size = 4369145 },
    { url = "https://files.pythonhosted.org/packages/de/7c/7433122d1cfadc740f577cb55526fdc39129a648ac65ce64db2eb7209277/pillow-11.1.0-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:3764d53e09cdedd91bee65c2527815d315c6b90d7b8b79759cc48d7bf5d4f114", size = 4496340 },
    { url = "https://files.pythonhosted.org/packages/25/46/dd94b93ca6bd555588835f2504bd90c00d5438fe131cf01cfa0c5131a19d/pillow-11.1.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:31eba6bbdd27dde97b0174ddf0297d7a9c3a507a8a1480e1e60ef914fe23d352", size = 4296906 },
    { url = "https://files.pythonhosted.org/packages/a8/28/2f9d32014dfc7753e586db9add35b8a41b7a3b46540e965cb6d6bc607bd2/pillow-11.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b5d658fbd9f0d6eea113aea286b21d3cd4d3fd978157cbf2447a6035916506d3", size = 4431759 },
    { url = "https://files.pythonhosted.org/packages/33/48/19c2cbe7403870fbe8b7737d19eb013f46299cdfe4501573367f6396c775/pillow-11.1.0-cp313-cp313-win32.whl", hash = "sha256:f86d3a7a9af5d826744fabf4afd15b9dfef44fe69a98541f666f66fbb8d3fef9", size = 2291657 },
    { url = "https://files.pythonhosted.org/packages/3b/ad/285c556747d34c399f332ba7c1a595ba245796ef3e22eae190f5364bb62b/pillow-11.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:593c5fd6be85da83656b93ffcccc2312d2d149d251e98588b14fbc288fd8909c", size = 2626304 },
    { url = "https://files.pythonhosted.org/packages/e5/7b/ef35a71163bf36db06e9c8729608f78dedf032fc8313d19bd4be5c2588f3/pillow-11.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:11633d58b6ee5733bde153a8dafd25e505ea3d32e261accd388827ee987baf65", size = 2375117 },
    { url = "https://files.pythonhosted.org/packages/79/30/77f54228401e84d6791354888549b45824ab0ffde659bafa67956303a09f/pillow-11.1.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:70ca5ef3b3b1c4a0812b5c63c57c23b63e53bc38e758b37a951e5bc466449861", size = 3230060 },
    { url = "https://files.pythonhosted.org/packages/ce/b1/56723b74b07dd64c1010fee011951ea9c35a43d8020acd03111f14298225/pillow-11.1.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:8000376f139d4d38d6851eb149b321a52bb8893a88dae8ee7d95840431977081", size = 3106192 },
    { url = "https://files.pythonhosted.org/packages/e1/cd/7bf7180e08f80a4dcc6b4c3a0aa9e0b0ae57168562726a05dc8aa8fa66b0/pillow-11.1.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9ee85f0696a17dd28fbcfceb59f9510aa71934b483d1f5601d1030c3c8304f3c", size = 4446805 },
    { url = "https://files.pythonhosted.org/packages/97/42/87c856ea30c8ed97e8efbe672b58c8304dee0573f8c7cab62ae9e31db6ae/pillow-11.1.0-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:dd0e081319328928531df7a0e63621caf67652c8464303fd102141b785ef9547", size = 4530623 },
    { url = "https://files.pythonhosted.org/packages/ff/41/026879e90c84a88e33fb00cc6bd915ac2743c67e87a18f80270dfe3c2041/pillow-11.1.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:e63e4e5081de46517099dc30abe418122f54531a6ae2ebc8680bcd7096860eab", size = 4465191 },
    { url = "https://files.pythonhosted.org/packages/e5/fb/a7960e838bc5df57a2ce23183bfd2290d97c33028b96bde332a9057834d3/pillow-11.1.0-cp313-cp313t-win32.whl", hash = "sha256:dda60aa465b861324e65a78c9f5cf0f4bc713e4309f83bc387be158b077963d9", size = 2295494 },
    { url = "https://files.pythonhosted.org/packages/d7/6c/6ec83ee2f6f0fda8d4cf89045c6be4b0373ebfc363ba8538f8c999f63fcd/pillow-11.1.0-cp313-cp313t-win_amd64.whl", hash = "sha256:ad5db5781c774ab9a9b2c4302bbf0c1014960a0a7be63278d13ae6fdf88126fe", size = 2631595 },
    { url = "https://files.pythonhosted.org/packages/cf/6c/41c21c6c8af92b9fea313aa47c75de49e2f9a467964ee33eb0135d47eb64/pillow-11.1.0-cp313-cp313t-win_arm64.whl", hash = "sha256:67cd427c68926108778a9005f2a04adbd5e67c442ed21d95389fe1d595458756", size = 2377651 },
]

[[package]]
name = "protobuf"
version = "5.29.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f7/d1/e0a911544ca9993e0f17ce6d3cc0932752356c1b0a834397f28e63479344/protobuf-5.29.3.tar.gz", hash = "sha256:5da0f41edaf117bde316404bad1a486cb4ededf8e4a54891296f648e8e076620", size = 424945 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/7a/1e38f3cafa022f477ca0f57a1f49962f21ad25850c3ca0acd3b9d0091518/protobuf-5.29.3-cp310-abi3-win32.whl", hash = "sha256:3ea51771449e1035f26069c4c7fd51fba990d07bc55ba80701c78f886bf9c888", size = 422708 },
    { url = "https://files.pythonhosted.org/packages/61/fa/aae8e10512b83de633f2646506a6d835b151edf4b30d18d73afd01447253/protobuf-5.29.3-cp310-abi3-win_amd64.whl", hash = "sha256:a4fa6f80816a9a0678429e84973f2f98cbc218cca434abe8db2ad0bffc98503a", size = 434508 },
    { url = "https://files.pythonhosted.org/packages/dd/04/3eaedc2ba17a088961d0e3bd396eac764450f431621b58a04ce898acd126/protobuf-5.29.3-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:a8434404bbf139aa9e1300dbf989667a83d42ddda9153d8ab76e0d5dcaca484e", size = 417825 },
    { url = "https://files.pythonhosted.org/packages/4f/06/7c467744d23c3979ce250397e26d8ad8eeb2bea7b18ca12ad58313c1b8d5/protobuf-5.29.3-cp38-abi3-manylinux2014_aarch64.whl", hash = "sha256:daaf63f70f25e8689c072cfad4334ca0ac1d1e05a92fc15c54eb9cf23c3efd84", size = 319573 },
    { url = "https://files.pythonhosted.org/packages/a8/45/2ebbde52ad2be18d3675b6bee50e68cd73c9e0654de77d595540b5129df8/protobuf-5.29.3-cp38-abi3-manylinux2014_x86_64.whl", hash = "sha256:c027e08a08be10b67c06bf2370b99c811c466398c357e615ca88c91c07f0910f", size = 319672 },
    { url = "https://files.pythonhosted.org/packages/fd/b2/ab07b09e0f6d143dfb839693aa05765257bceaa13d03bf1a696b78323e7a/protobuf-5.29.3-py3-none-any.whl", hash = "sha256:0a18ed4a24198528f2333802eb075e59dea9d679ab7a6c5efb017a59004d849f", size = 172550 },
]

[[package]]
name = "psycopg2-binary"
version = "2.9.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cb/0e/bdc8274dc0585090b4e3432267d7be4dfbfd8971c0fa59167c711105a6bf/psycopg2-binary-2.9.10.tar.gz", hash = "sha256:4b3df0e6990aa98acda57d983942eff13d824135fe2250e6522edaa782a06de2", size = 385764 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9c/8f/9feb01291d0d7a0a4c6a6bab24094135c2b59c6a81943752f632c75896d6/psycopg2_binary-2.9.10-cp311-cp311-macosx_12_0_x86_64.whl", hash = "sha256:04392983d0bb89a8717772a193cfaac58871321e3ec69514e1c4e0d4957b5aff", size = 3043397 },
    { url = "https://files.pythonhosted.org/packages/15/30/346e4683532011561cd9c8dfeac6a8153dd96452fee0b12666058ab7893c/psycopg2_binary-2.9.10-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:1a6784f0ce3fec4edc64e985865c17778514325074adf5ad8f80636cd029ef7c", size = 3274806 },
    { url = "https://files.pythonhosted.org/packages/66/6e/4efebe76f76aee7ec99166b6c023ff8abdc4e183f7b70913d7c047701b79/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b5f86c56eeb91dc3135b3fd8a95dc7ae14c538a2f3ad77a19645cf55bab1799c", size = 2851370 },
    { url = "https://files.pythonhosted.org/packages/7f/fd/ff83313f86b50f7ca089b161b8e0a22bb3c319974096093cd50680433fdb/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:2b3d2491d4d78b6b14f76881905c7a8a8abcf974aad4a8a0b065273a0ed7a2cb", size = 3080780 },
    { url = "https://files.pythonhosted.org/packages/e6/c4/bfadd202dcda8333a7ccafdc51c541dbdfce7c2c7cda89fa2374455d795f/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2286791ececda3a723d1910441c793be44625d86d1a4e79942751197f4d30341", size = 3264583 },
    { url = "https://files.pythonhosted.org/packages/5d/f1/09f45ac25e704ac954862581f9f9ae21303cc5ded3d0b775532b407f0e90/psycopg2_binary-2.9.10-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:512d29bb12608891e349af6a0cccedce51677725a921c07dba6342beaf576f9a", size = 3019831 },
    { url = "https://files.pythonhosted.org/packages/9e/2e/9beaea078095cc558f215e38f647c7114987d9febfc25cb2beed7c3582a5/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:5a507320c58903967ef7384355a4da7ff3f28132d679aeb23572753cbf2ec10b", size = 2871822 },
    { url = "https://files.pythonhosted.org/packages/01/9e/ef93c5d93f3dc9fc92786ffab39e323b9aed066ba59fdc34cf85e2722271/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:6d4fa1079cab9018f4d0bd2db307beaa612b0d13ba73b5c6304b9fe2fb441ff7", size = 2820975 },
    { url = "https://files.pythonhosted.org/packages/a5/f0/049e9631e3268fe4c5a387f6fc27e267ebe199acf1bc1bc9cbde4bd6916c/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:851485a42dbb0bdc1edcdabdb8557c09c9655dfa2ca0460ff210522e073e319e", size = 2919320 },
    { url = "https://files.pythonhosted.org/packages/dc/9a/bcb8773b88e45fb5a5ea8339e2104d82c863a3b8558fbb2aadfe66df86b3/psycopg2_binary-2.9.10-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:35958ec9e46432d9076286dda67942ed6d968b9c3a6a2fd62b48939d1d78bf68", size = 2957617 },
    { url = "https://files.pythonhosted.org/packages/e2/6b/144336a9bf08a67d217b3af3246abb1d027095dab726f0687f01f43e8c03/psycopg2_binary-2.9.10-cp311-cp311-win32.whl", hash = "sha256:ecced182e935529727401b24d76634a357c71c9275b356efafd8a2a91ec07392", size = 1024618 },
    { url = "https://files.pythonhosted.org/packages/61/69/3b3d7bd583c6d3cbe5100802efa5beacaacc86e37b653fc708bf3d6853b8/psycopg2_binary-2.9.10-cp311-cp311-win_amd64.whl", hash = "sha256:ee0e8c683a7ff25d23b55b11161c2663d4b099770f6085ff0a20d4505778d6b4", size = 1163816 },
    { url = "https://files.pythonhosted.org/packages/49/7d/465cc9795cf76f6d329efdafca74693714556ea3891813701ac1fee87545/psycopg2_binary-2.9.10-cp312-cp312-macosx_12_0_x86_64.whl", hash = "sha256:880845dfe1f85d9d5f7c412efea7a08946a46894537e4e5d091732eb1d34d9a0", size = 3044771 },
    { url = "https://files.pythonhosted.org/packages/8b/31/6d225b7b641a1a2148e3ed65e1aa74fc86ba3fee850545e27be9e1de893d/psycopg2_binary-2.9.10-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:9440fa522a79356aaa482aa4ba500b65f28e5d0e63b801abf6aa152a29bd842a", size = 3275336 },
    { url = "https://files.pythonhosted.org/packages/30/b7/a68c2b4bff1cbb1728e3ec864b2d92327c77ad52edcd27922535a8366f68/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e3923c1d9870c49a2d44f795df0c889a22380d36ef92440ff618ec315757e539", size = 2851637 },
    { url = "https://files.pythonhosted.org/packages/0b/b1/cfedc0e0e6f9ad61f8657fd173b2f831ce261c02a08c0b09c652b127d813/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7b2c956c028ea5de47ff3a8d6b3cc3330ab45cf0b7c3da35a2d6ff8420896526", size = 3082097 },
    { url = "https://files.pythonhosted.org/packages/18/ed/0a8e4153c9b769f59c02fb5e7914f20f0b2483a19dae7bf2db54b743d0d0/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f758ed67cab30b9a8d2833609513ce4d3bd027641673d4ebc9c067e4d208eec1", size = 3264776 },
    { url = "https://files.pythonhosted.org/packages/10/db/d09da68c6a0cdab41566b74e0a6068a425f077169bed0946559b7348ebe9/psycopg2_binary-2.9.10-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8cd9b4f2cfab88ed4a9106192de509464b75a906462fb846b936eabe45c2063e", size = 3020968 },
    { url = "https://files.pythonhosted.org/packages/94/28/4d6f8c255f0dfffb410db2b3f9ac5218d959a66c715c34cac31081e19b95/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6dc08420625b5a20b53551c50deae6e231e6371194fa0651dbe0fb206452ae1f", size = 2872334 },
    { url = "https://files.pythonhosted.org/packages/05/f7/20d7bf796593c4fea95e12119d6cc384ff1f6141a24fbb7df5a668d29d29/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:d7cd730dfa7c36dbe8724426bf5612798734bff2d3c3857f36f2733f5bfc7c00", size = 2822722 },
    { url = "https://files.pythonhosted.org/packages/4d/e4/0c407ae919ef626dbdb32835a03b6737013c3cc7240169843965cada2bdf/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:155e69561d54d02b3c3209545fb08938e27889ff5a10c19de8d23eb5a41be8a5", size = 2920132 },
    { url = "https://files.pythonhosted.org/packages/2d/70/aa69c9f69cf09a01da224909ff6ce8b68faeef476f00f7ec377e8f03be70/psycopg2_binary-2.9.10-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:c3cc28a6fd5a4a26224007712e79b81dbaee2ffb90ff406256158ec4d7b52b47", size = 2959312 },
    { url = "https://files.pythonhosted.org/packages/d3/bd/213e59854fafe87ba47814bf413ace0dcee33a89c8c8c814faca6bc7cf3c/psycopg2_binary-2.9.10-cp312-cp312-win32.whl", hash = "sha256:ec8a77f521a17506a24a5f626cb2aee7850f9b69a0afe704586f63a464f3cd64", size = 1025191 },
    { url = "https://files.pythonhosted.org/packages/92/29/06261ea000e2dc1e22907dbbc483a1093665509ea586b29b8986a0e56733/psycopg2_binary-2.9.10-cp312-cp312-win_amd64.whl", hash = "sha256:18c5ee682b9c6dd3696dad6e54cc7ff3a1a9020df6a5c0f861ef8bfd338c3ca0", size = 1164031 },
    { url = "https://files.pythonhosted.org/packages/3e/30/d41d3ba765609c0763505d565c4d12d8f3c79793f0d0f044ff5a28bf395b/psycopg2_binary-2.9.10-cp313-cp313-macosx_12_0_x86_64.whl", hash = "sha256:26540d4a9a4e2b096f1ff9cce51253d0504dca5a85872c7f7be23be5a53eb18d", size = 3044699 },
    { url = "https://files.pythonhosted.org/packages/35/44/257ddadec7ef04536ba71af6bc6a75ec05c5343004a7ec93006bee66c0bc/psycopg2_binary-2.9.10-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:e217ce4d37667df0bc1c397fdcd8de5e81018ef305aed9415c3b093faaeb10fb", size = 3275245 },
    { url = "https://files.pythonhosted.org/packages/1b/11/48ea1cd11de67f9efd7262085588790a95d9dfcd9b8a687d46caf7305c1a/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:245159e7ab20a71d989da00f280ca57da7641fa2cdcf71749c193cea540a74f7", size = 2851631 },
    { url = "https://files.pythonhosted.org/packages/62/e0/62ce5ee650e6c86719d621a761fe4bc846ab9eff8c1f12b1ed5741bf1c9b/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3c4ded1a24b20021ebe677b7b08ad10bf09aac197d6943bfe6fec70ac4e4690d", size = 3082140 },
    { url = "https://files.pythonhosted.org/packages/27/ce/63f946c098611f7be234c0dd7cb1ad68b0b5744d34f68062bb3c5aa510c8/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3abb691ff9e57d4a93355f60d4f4c1dd2d68326c968e7db17ea96df3c023ef73", size = 3264762 },
    { url = "https://files.pythonhosted.org/packages/43/25/c603cd81402e69edf7daa59b1602bd41eb9859e2824b8c0855d748366ac9/psycopg2_binary-2.9.10-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8608c078134f0b3cbd9f89b34bd60a943b23fd33cc5f065e8d5f840061bd0673", size = 3020967 },
    { url = "https://files.pythonhosted.org/packages/5f/d6/8708d8c6fca531057fa170cdde8df870e8b6a9b136e82b361c65e42b841e/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:230eeae2d71594103cd5b93fd29d1ace6420d0b86f4778739cb1a5a32f607d1f", size = 2872326 },
    { url = "https://files.pythonhosted.org/packages/ce/ac/5b1ea50fc08a9df82de7e1771537557f07c2632231bbab652c7e22597908/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:bb89f0a835bcfc1d42ccd5f41f04870c1b936d8507c6df12b7737febc40f0909", size = 2822712 },
    { url = "https://files.pythonhosted.org/packages/c4/fc/504d4503b2abc4570fac3ca56eb8fed5e437bf9c9ef13f36b6621db8ef00/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:f0c2d907a1e102526dd2986df638343388b94c33860ff3bbe1384130828714b1", size = 2920155 },
    { url = "https://files.pythonhosted.org/packages/b2/d1/323581e9273ad2c0dbd1902f3fb50c441da86e894b6e25a73c3fda32c57e/psycopg2_binary-2.9.10-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f8157bed2f51db683f31306aa497311b560f2265998122abe1dce6428bd86567", size = 2959356 },
    { url = "https://files.pythonhosted.org/packages/08/50/d13ea0a054189ae1bc21af1d85b6f8bb9bbc5572991055d70ad9006fe2d6/psycopg2_binary-2.9.10-cp313-cp313-win_amd64.whl", hash = "sha256:27422aa5f11fbcd9b18da48373eb67081243662f9b46e6fd07c3eb46e4535142", size = 2569224 },
]

[[package]]
name = "pyarrow"
version = "19.0.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7f/09/a9046344212690f0632b9c709f9bf18506522feb333c894d0de81d62341a/pyarrow-19.0.1.tar.gz", hash = "sha256:3bf266b485df66a400f282ac0b6d1b500b9d2ae73314a153dbe97d6d5cc8a99e", size = 1129437 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/55/f1a8d838ec07fe3ca53edbe76f782df7b9aafd4417080eebf0b42aab0c52/pyarrow-19.0.1-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:cc55d71898ea30dc95900297d191377caba257612f384207fe9f8293b5850f90", size = 30713987 },
    { url = "https://files.pythonhosted.org/packages/13/12/428861540bb54c98a140ae858a11f71d041ef9e501e6b7eb965ca7909505/pyarrow-19.0.1-cp311-cp311-macosx_12_0_x86_64.whl", hash = "sha256:7a544ec12de66769612b2d6988c36adc96fb9767ecc8ee0a4d270b10b1c51e00", size = 32135613 },
    { url = "https://files.pythonhosted.org/packages/2f/8a/23d7cc5ae2066c6c736bce1db8ea7bc9ac3ef97ac7e1c1667706c764d2d9/pyarrow-19.0.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0148bb4fc158bfbc3d6dfe5001d93ebeed253793fff4435167f6ce1dc4bddeae", size = 41149147 },
    { url = "https://files.pythonhosted.org/packages/a2/7a/845d151bb81a892dfb368bf11db584cf8b216963ccce40a5cf50a2492a18/pyarrow-19.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f24faab6ed18f216a37870d8c5623f9c044566d75ec586ef884e13a02a9d62c5", size = 42178045 },
    { url = "https://files.pythonhosted.org/packages/a7/31/e7282d79a70816132cf6cae7e378adfccce9ae10352d21c2fecf9d9756dd/pyarrow-19.0.1-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:4982f8e2b7afd6dae8608d70ba5bd91699077323f812a0448d8b7abdff6cb5d3", size = 40532998 },
    { url = "https://files.pythonhosted.org/packages/b8/82/20f3c290d6e705e2ee9c1fa1d5a0869365ee477e1788073d8b548da8b64c/pyarrow-19.0.1-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:49a3aecb62c1be1d822f8bf629226d4a96418228a42f5b40835c1f10d42e4db6", size = 42084055 },
    { url = "https://files.pythonhosted.org/packages/ff/77/e62aebd343238863f2c9f080ad2ef6ace25c919c6ab383436b5b81cbeef7/pyarrow-19.0.1-cp311-cp311-win_amd64.whl", hash = "sha256:008a4009efdb4ea3d2e18f05cd31f9d43c388aad29c636112c2966605ba33466", size = 25283133 },
    { url = "https://files.pythonhosted.org/packages/78/b4/94e828704b050e723f67d67c3535cf7076c7432cd4cf046e4bb3b96a9c9d/pyarrow-19.0.1-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:80b2ad2b193e7d19e81008a96e313fbd53157945c7be9ac65f44f8937a55427b", size = 30670749 },
    { url = "https://files.pythonhosted.org/packages/7e/3b/4692965e04bb1df55e2c314c4296f1eb12b4f3052d4cf43d29e076aedf66/pyarrow-19.0.1-cp312-cp312-macosx_12_0_x86_64.whl", hash = "sha256:ee8dec072569f43835932a3b10c55973593abc00936c202707a4ad06af7cb294", size = 32128007 },
    { url = "https://files.pythonhosted.org/packages/22/f7/2239af706252c6582a5635c35caa17cb4d401cd74a87821ef702e3888957/pyarrow-19.0.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4d5d1ec7ec5324b98887bdc006f4d2ce534e10e60f7ad995e7875ffa0ff9cb14", size = 41144566 },
    { url = "https://files.pythonhosted.org/packages/fb/e3/c9661b2b2849cfefddd9fd65b64e093594b231b472de08ff658f76c732b2/pyarrow-19.0.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f3ad4c0eb4e2a9aeb990af6c09e6fa0b195c8c0e7b272ecc8d4d2b6574809d34", size = 42202991 },
    { url = "https://files.pythonhosted.org/packages/fe/4f/a2c0ed309167ef436674782dfee4a124570ba64299c551e38d3fdaf0a17b/pyarrow-19.0.1-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:d383591f3dcbe545f6cc62daaef9c7cdfe0dff0fb9e1c8121101cabe9098cfa6", size = 40507986 },
    { url = "https://files.pythonhosted.org/packages/27/2e/29bb28a7102a6f71026a9d70d1d61df926887e36ec797f2e6acfd2dd3867/pyarrow-19.0.1-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:b4c4156a625f1e35d6c0b2132635a237708944eb41df5fbe7d50f20d20c17832", size = 42087026 },
    { url = "https://files.pythonhosted.org/packages/16/33/2a67c0f783251106aeeee516f4806161e7b481f7d744d0d643d2f30230a5/pyarrow-19.0.1-cp312-cp312-win_amd64.whl", hash = "sha256:5bd1618ae5e5476b7654c7b55a6364ae87686d4724538c24185bbb2952679960", size = 25250108 },
    { url = "https://files.pythonhosted.org/packages/2b/8d/275c58d4b00781bd36579501a259eacc5c6dfb369be4ddeb672ceb551d2d/pyarrow-19.0.1-cp313-cp313-macosx_12_0_arm64.whl", hash = "sha256:e45274b20e524ae5c39d7fc1ca2aa923aab494776d2d4b316b49ec7572ca324c", size = 30653552 },
    { url = "https://files.pythonhosted.org/packages/a0/9e/e6aca5cc4ef0c7aec5f8db93feb0bde08dbad8c56b9014216205d271101b/pyarrow-19.0.1-cp313-cp313-macosx_12_0_x86_64.whl", hash = "sha256:d9dedeaf19097a143ed6da37f04f4051aba353c95ef507764d344229b2b740ae", size = 32103413 },
    { url = "https://files.pythonhosted.org/packages/6a/fa/a7033f66e5d4f1308c7eb0dfcd2ccd70f881724eb6fd1776657fdf65458f/pyarrow-19.0.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6ebfb5171bb5f4a52319344ebbbecc731af3f021e49318c74f33d520d31ae0c4", size = 41134869 },
    { url = "https://files.pythonhosted.org/packages/2d/92/34d2569be8e7abdc9d145c98dc410db0071ac579b92ebc30da35f500d630/pyarrow-19.0.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f2a21d39fbdb948857f67eacb5bbaaf36802de044ec36fbef7a1c8f0dd3a4ab2", size = 42192626 },
    { url = "https://files.pythonhosted.org/packages/0a/1f/80c617b1084fc833804dc3309aa9d8daacd46f9ec8d736df733f15aebe2c/pyarrow-19.0.1-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:99bc1bec6d234359743b01e70d4310d0ab240c3d6b0da7e2a93663b0158616f6", size = 40496708 },
    { url = "https://files.pythonhosted.org/packages/e6/90/83698fcecf939a611c8d9a78e38e7fed7792dcc4317e29e72cf8135526fb/pyarrow-19.0.1-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:1b93ef2c93e77c442c979b0d596af45e4665d8b96da598db145b0fec014b9136", size = 42075728 },
    { url = "https://files.pythonhosted.org/packages/40/49/2325f5c9e7a1c125c01ba0c509d400b152c972a47958768e4e35e04d13d8/pyarrow-19.0.1-cp313-cp313-win_amd64.whl", hash = "sha256:d9d46e06846a41ba906ab25302cf0fd522f81aa2a85a71021826f34639ad31ef", size = 25242568 },
    { url = "https://files.pythonhosted.org/packages/3f/72/135088d995a759d4d916ec4824cb19e066585b4909ebad4ab196177aa825/pyarrow-19.0.1-cp313-cp313t-macosx_12_0_arm64.whl", hash = "sha256:c0fe3dbbf054a00d1f162fda94ce236a899ca01123a798c561ba307ca38af5f0", size = 30702371 },
    { url = "https://files.pythonhosted.org/packages/2e/01/00beeebd33d6bac701f20816a29d2018eba463616bbc07397fdf99ac4ce3/pyarrow-19.0.1-cp313-cp313t-macosx_12_0_x86_64.whl", hash = "sha256:96606c3ba57944d128e8a8399da4812f56c7f61de8c647e3470b417f795d0ef9", size = 32116046 },
    { url = "https://files.pythonhosted.org/packages/1f/c9/23b1ea718dfe967cbd986d16cf2a31fe59d015874258baae16d7ea0ccabc/pyarrow-19.0.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8f04d49a6b64cf24719c080b3c2029a3a5b16417fd5fd7c4041f94233af732f3", size = 41091183 },
    { url = "https://files.pythonhosted.org/packages/3a/d4/b4a3aa781a2c715520aa8ab4fe2e7fa49d33a1d4e71c8fc6ab7b5de7a3f8/pyarrow-19.0.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5a9137cf7e1640dce4c190551ee69d478f7121b5c6f323553b319cac936395f6", size = 42171896 },
    { url = "https://files.pythonhosted.org/packages/23/1b/716d4cd5a3cbc387c6e6745d2704c4b46654ba2668260d25c402626c5ddb/pyarrow-19.0.1-cp313-cp313t-manylinux_2_28_aarch64.whl", hash = "sha256:7c1bca1897c28013db5e4c83944a2ab53231f541b9e0c3f4791206d0c0de389a", size = 40464851 },
    { url = "https://files.pythonhosted.org/packages/ed/bd/54907846383dcc7ee28772d7e646f6c34276a17da740002a5cefe90f04f7/pyarrow-19.0.1-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:58d9397b2e273ef76264b45531e9d552d8ec8a6688b7390b5be44c02a37aade8", size = 42085744 },
]

[[package]]
name = "pydeck"
version = "0.9.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jinja2" },
    { name = "numpy" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a1/ca/40e14e196864a0f61a92abb14d09b3d3da98f94ccb03b49cf51688140dab/pydeck-0.9.1.tar.gz", hash = "sha256:f74475ae637951d63f2ee58326757f8d4f9cd9f2a457cf42950715003e2cb605", size = 3832240 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ab/4c/b888e6cf58bd9db9c93f40d1c6be8283ff49d88919231afe93a6bcf61626/pydeck-0.9.1-py2.py3-none-any.whl", hash = "sha256:b3f75ba0d273fc917094fa61224f3f6076ca8752b93d46faf3bcfd9f9d59b038", size = 6900403 },
]

[[package]]
name = "pygments"
version = "2.19.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7c/2d/c3338d48ea6cc0feb8446d8e6937e1408088a72a39937982cc6111d17f84/pygments-2.19.1.tar.gz", hash = "sha256:61c16d2a8576dc0649d9f39e089b5f02bcd27fba10d8fb4dcc28173f7a45151f", size = 4968581 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0b/9fcc47d19c48b59121088dd6da2488a49d5f72dacf8262e2790a1d2c7d15/pygments-2.19.1-py3-none-any.whl", hash = "sha256:9ea1544ad55cecf4b8242fab6dd35a93bbce657034b0611ee383099054ab6d8c", size = 1225293 },
]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "six" },
]
sdist = { url = "https://files.pythonhosted.org/packages/66/c0/0c8b6ad9f17a802ee498c46e004a0eb49bc148f2fd230864601a86dcf6db/python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3", size = 342432 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427", size = 229892 },
]

[[package]]
name = "pytz"
version = "2025.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5f/57/df1c9157c8d5a05117e455d66fd7cf6dbc46974f832b1058ed4856785d8a/pytz-2025.1.tar.gz", hash = "sha256:c2db42be2a2518b28e65f9207c4d05e6ff547d1efa4086469ef855e4ab70178e", size = 319617 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/eb/38/ac33370d784287baa1c3d538978b5e2ea064d4c1b93ffbd12826c190dd10/pytz-2025.1-py2.py3-none-any.whl", hash = "sha256:89dd22dca55b46eac6eda23b2d72721bf1bdfef212645d81513ef5d03038de57", size = 507930 },
]

[[package]]
name = "referencing"
version = "0.36.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "rpds-py" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/2f/db/98b5c277be99dd18bfd91dd04e1b759cad18d1a338188c936e92f921c7e2/referencing-0.36.2.tar.gz", hash = "sha256:df2e89862cd09deabbdba16944cc3f10feb6b3e6f18e902f7cc25609a34775aa", size = 74744 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c1/b1/3baf80dc6d2b7bc27a95a67752d0208e410351e3feb4eb78de5f77454d8d/referencing-0.36.2-py3-none-any.whl", hash = "sha256:e8699adbbf8b5c7de96d8ffa0eb5c158b3beafce084968e2ea8bb08c6794dcd0", size = 26775 },
]

[[package]]
name = "repl-nix-workspace"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "pandas" },
    { name = "psycopg2-binary" },
    { name = "reportlab" },
    { name = "sqlalchemy" },
    { name = "streamlit" },
]

[package.metadata]
requires-dist = [
    { name = "pandas", specifier = ">=2.2.3" },
    { name = "psycopg2-binary", specifier = ">=2.9.10" },
    { name = "reportlab", specifier = ">=4.3.1" },
    { name = "sqlalchemy", specifier = ">=2.0.38" },
    { name = "streamlit", specifier = ">=1.42.2" },
]

[[package]]
name = "reportlab"
version = "4.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "chardet" },
    { name = "pillow" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a7/5c/9b23c8a9a69f2bc1f1268ed545f393a60b59cbe5f9d861a28b676f809729/reportlab-4.3.1.tar.gz", hash = "sha256:230f78b21667194d8490ac9d12958d5c14686352db7fbe03b95140fafdf5aa97", size = 3499248 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ce/6b/42805895ed08a314a01be6110584b5d059328386988ddbc4f8f10014d30e/reportlab-4.3.1-py3-none-any.whl", hash = "sha256:0f37dd16652db3ef84363cf744632a28c38bd480d5bf94683466852d7bb678dd", size = 1949468 },
]

[[package]]
name = "requests"
version = "2.32.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/63/70/2bf7780ad2d390a8d301ad0b550f1581eadbd9a20f896afe06353c2a2913/requests-2.32.3.tar.gz", hash = "sha256:55365417734eb18255590a9ff9eb97e9e1da868d4ccd6402399eaf68af20a760", size = 131218 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl", hash = "sha256:70761cfe03c773ceb22aa2f671b4757976145175cdfca038c02654d061d6dcc6", size = 64928 },
]

[[package]]
name = "rich"
version = "13.9.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ab/3a/0316b28d0761c6734d6bc14e770d85506c986c85ffb239e688eeaab2c2bc/rich-13.9.4.tar.gz", hash = "sha256:439594978a49a09530cff7ebc4b5c7103ef57baf48d5ea3184f21d9a2befa098", size = 223149 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/19/71/39c7c0d87f8d4e6c020a393182060eaefeeae6c01dab6a84ec346f2567df/rich-13.9.4-py3-none-any.whl", hash = "sha256:6049d5e6ec054bf2779ab3358186963bac2ea89175919d699e378b99738c2a90", size = 242424 },
]

[[package]]
name = "rpds-py"
version = "0.23.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0a/79/2ce611b18c4fd83d9e3aecb5cba93e1917c050f556db39842889fa69b79f/rpds_py-0.23.1.tar.gz", hash = "sha256:7f3240dcfa14d198dba24b8b9cb3b108c06b68d45b7babd9eefc1038fdf7e707", size = 26806 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1c/67/6e5d4234bb9dee062ffca2a5f3c7cd38716317d6760ec235b175eed4de2c/rpds_py-0.23.1-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:b79f5ced71efd70414a9a80bbbfaa7160da307723166f09b69773153bf17c590", size = 372264 },
    { url = "https://files.pythonhosted.org/packages/a7/0a/3dedb2daee8e783622427f5064e2d112751d8276ee73aa5409f000a132f4/rpds_py-0.23.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c9e799dac1ffbe7b10c1fd42fe4cd51371a549c6e108249bde9cd1200e8f59b4", size = 356883 },
    { url = "https://files.pythonhosted.org/packages/ed/fc/e1acef44f9c24b05fe5434b235f165a63a52959ac655e3f7a55726cee1a4/rpds_py-0.23.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:721f9c4011b443b6e84505fc00cc7aadc9d1743f1c988e4c89353e19c4a968ee", size = 385624 },
    { url = "https://files.pythonhosted.org/packages/97/0a/a05951f6465d01622720c03ef6ef31adfbe865653e05ed7c45837492f25e/rpds_py-0.23.1-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:f88626e3f5e57432e6191cd0c5d6d6b319b635e70b40be2ffba713053e5147dd", size = 391500 },
    { url = "https://files.pythonhosted.org/packages/ea/2e/cca0583ec0690ea441dceae23c0673b99755710ea22f40bccf1e78f41481/rpds_py-0.23.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:285019078537949cecd0190f3690a0b0125ff743d6a53dfeb7a4e6787af154f5", size = 444869 },
    { url = "https://files.pythonhosted.org/packages/cc/e6/95cda68b33a6d814d1e96b0e406d231ed16629101460d1740e92f03365e6/rpds_py-0.23.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b92f5654157de1379c509b15acec9d12ecf6e3bc1996571b6cb82a4302060447", size = 444930 },
    { url = "https://files.pythonhosted.org/packages/5f/a7/e94cdb73411ae9c11414d3c7c9a6ad75d22ad4a8d094fb45a345ba9e3018/rpds_py-0.23.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e768267cbe051dd8d1c5305ba690bb153204a09bf2e3de3ae530de955f5b5580", size = 386254 },
    { url = "https://files.pythonhosted.org/packages/dd/c5/a4a943d90a39e85efd1e04b1ad5129936786f9a9aa27bb7be8fc5d9d50c9/rpds_py-0.23.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c5334a71f7dc1160382d45997e29f2637c02f8a26af41073189d79b95d3321f1", size = 417090 },
    { url = "https://files.pythonhosted.org/packages/0c/a0/80d0013b12428d1fce0ab4e71829400b0a32caec12733c79e6109f843342/rpds_py-0.23.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d6adb81564af0cd428910f83fa7da46ce9ad47c56c0b22b50872bc4515d91966", size = 557639 },
    { url = "https://files.pythonhosted.org/packages/a6/92/ec2e6980afb964a2cd7a99cbdef1f6c01116abe94b42cbe336ac93dd11c2/rpds_py-0.23.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:cafa48f2133d4daa028473ede7d81cd1b9f9e6925e9e4003ebdf77010ee02f35", size = 584572 },
    { url = "https://files.pythonhosted.org/packages/3d/ce/75b6054db34a390789a82523790717b27c1bd735e453abb429a87c4f0f26/rpds_py-0.23.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0fced9fd4a07a1ded1bac7e961ddd9753dd5d8b755ba8e05acba54a21f5f1522", size = 553028 },
    { url = "https://files.pythonhosted.org/packages/cc/24/f45abe0418c06a5cba0f846e967aa27bac765acd927aabd857c21319b8cc/rpds_py-0.23.1-cp311-cp311-win32.whl", hash = "sha256:243241c95174b5fb7204c04595852fe3943cc41f47aa14c3828bc18cd9d3b2d6", size = 220862 },
    { url = "https://files.pythonhosted.org/packages/2d/a6/3c0880e8bbfc36451ef30dc416266f6d2934705e468db5d21c8ba0ab6400/rpds_py-0.23.1-cp311-cp311-win_amd64.whl", hash = "sha256:11dd60b2ffddba85715d8a66bb39b95ddbe389ad2cfcf42c833f1bcde0878eaf", size = 232953 },
    { url = "https://files.pythonhosted.org/packages/f3/8c/d17efccb9f5b9137ddea706664aebae694384ae1d5997c0202093e37185a/rpds_py-0.23.1-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:3902df19540e9af4cc0c3ae75974c65d2c156b9257e91f5101a51f99136d834c", size = 364369 },
    { url = "https://files.pythonhosted.org/packages/6e/c0/ab030f696b5c573107115a88d8d73d80f03309e60952b64c584c70c659af/rpds_py-0.23.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:66f8d2a17e5838dd6fb9be6baaba8e75ae2f5fa6b6b755d597184bfcd3cb0eba", size = 349965 },
    { url = "https://files.pythonhosted.org/packages/b3/55/b40170f5a079c4fb0b6a82b299689e66e744edca3c3375a8b160fb797660/rpds_py-0.23.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:112b8774b0b4ee22368fec42749b94366bd9b536f8f74c3d4175d4395f5cbd31", size = 389064 },
    { url = "https://files.pythonhosted.org/packages/ab/1c/b03a912c59ec7c1e16b26e587b9dfa8ddff3b07851e781e8c46e908a365a/rpds_py-0.23.1-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e0df046f2266e8586cf09d00588302a32923eb6386ced0ca5c9deade6af9a149", size = 397741 },
    { url = "https://files.pythonhosted.org/packages/52/6f/151b90792b62fb6f87099bcc9044c626881fdd54e31bf98541f830b15cea/rpds_py-0.23.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0f3288930b947cbebe767f84cf618d2cbe0b13be476e749da0e6a009f986248c", size = 448784 },
    { url = "https://files.pythonhosted.org/packages/71/2a/6de67c0c97ec7857e0e9e5cd7c52405af931b303eb1e5b9eff6c50fd9a2e/rpds_py-0.23.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ce473a2351c018b06dd8d30d5da8ab5a0831056cc53b2006e2a8028172c37ce5", size = 440203 },
    { url = "https://files.pythonhosted.org/packages/db/5e/e759cd1c276d98a4b1f464b17a9bf66c65d29f8f85754e27e1467feaa7c3/rpds_py-0.23.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d550d7e9e7d8676b183b37d65b5cd8de13676a738973d330b59dc8312df9c5dc", size = 391611 },
    { url = "https://files.pythonhosted.org/packages/1c/1e/2900358efcc0d9408c7289769cba4c0974d9db314aa884028ed7f7364f61/rpds_py-0.23.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e14f86b871ea74c3fddc9a40e947d6a5d09def5adc2076ee61fb910a9014fb35", size = 423306 },
    { url = "https://files.pythonhosted.org/packages/23/07/6c177e6d059f5d39689352d6c69a926ee4805ffdb6f06203570234d3d8f7/rpds_py-0.23.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:1bf5be5ba34e19be579ae873da515a2836a2166d8d7ee43be6ff909eda42b72b", size = 562323 },
    { url = "https://files.pythonhosted.org/packages/70/e4/f9097fd1c02b516fff9850792161eb9fc20a2fd54762f3c69eae0bdb67cb/rpds_py-0.23.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:d7031d493c4465dbc8d40bd6cafefef4bd472b17db0ab94c53e7909ee781b9ef", size = 588351 },
    { url = "https://files.pythonhosted.org/packages/87/39/5db3c6f326bfbe4576ae2af6435bd7555867d20ae690c786ff33659f293b/rpds_py-0.23.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:55ff4151cfd4bc635e51cfb1c59ac9f7196b256b12e3a57deb9e5742e65941ad", size = 557252 },
    { url = "https://files.pythonhosted.org/packages/fd/14/2d5ad292f144fa79bafb78d2eb5b8a3a91c358b6065443cb9c49b5d1fedf/rpds_py-0.23.1-cp312-cp312-win32.whl", hash = "sha256:a9d3b728f5a5873d84cba997b9d617c6090ca5721caaa691f3b1a78c60adc057", size = 222181 },
    { url = "https://files.pythonhosted.org/packages/a3/4f/0fce63e0f5cdd658e71e21abd17ac1bc9312741ebb8b3f74eeed2ebdf771/rpds_py-0.23.1-cp312-cp312-win_amd64.whl", hash = "sha256:b03a8d50b137ee758e4c73638b10747b7c39988eb8e6cd11abb7084266455165", size = 237426 },
    { url = "https://files.pythonhosted.org/packages/13/9d/b8b2c0edffb0bed15be17b6d5ab06216f2f47f9ee49259c7e96a3ad4ca42/rpds_py-0.23.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:4caafd1a22e5eaa3732acb7672a497123354bef79a9d7ceed43387d25025e935", size = 363672 },
    { url = "https://files.pythonhosted.org/packages/bd/c2/5056fa29e6894144d7ba4c938b9b0445f75836b87d2dd00ed4999dc45a8c/rpds_py-0.23.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:178f8a60fc24511c0eb756af741c476b87b610dba83270fce1e5a430204566a4", size = 349602 },
    { url = "https://files.pythonhosted.org/packages/b0/bc/33779a1bb0ee32d8d706b173825aab75c628521d23ce72a7c1e6a6852f86/rpds_py-0.23.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c632419c3870507ca20a37c8f8f5352317aca097639e524ad129f58c125c61c6", size = 388746 },
    { url = "https://files.pythonhosted.org/packages/62/0b/71db3e36b7780a619698ec82a9c87ab44ad7ca7f5480913e8a59ff76f050/rpds_py-0.23.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:698a79d295626ee292d1730bc2ef6e70a3ab135b1d79ada8fde3ed0047b65a10", size = 397076 },
    { url = "https://files.pythonhosted.org/packages/bb/2e/494398f613edf77ba10a916b1ddea2acce42ab0e3b62e2c70ffc0757ce00/rpds_py-0.23.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:271fa2184cf28bdded86bb6217c8e08d3a169fe0bbe9be5e8d96e8476b707122", size = 448399 },
    { url = "https://files.pythonhosted.org/packages/dd/53/4bd7f5779b1f463243ee5fdc83da04dd58a08f86e639dbffa7a35f969a84/rpds_py-0.23.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:b91cceb5add79ee563bd1f70b30896bd63bc5f78a11c1f00a1e931729ca4f1f4", size = 439764 },
    { url = "https://files.pythonhosted.org/packages/f6/55/b3c18c04a460d951bf8e91f2abf46ce5b6426fb69784166a6a25827cb90a/rpds_py-0.23.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f3a6cb95074777f1ecda2ca4fa7717caa9ee6e534f42b7575a8f0d4cb0c24013", size = 390662 },
    { url = "https://files.pythonhosted.org/packages/2a/65/cc463044a3cbd616029b2aa87a651cdee8288d2fdd7780b2244845e934c1/rpds_py-0.23.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:50fb62f8d8364978478b12d5f03bf028c6bc2af04082479299139dc26edf4c64", size = 422680 },
    { url = "https://files.pythonhosted.org/packages/fa/8e/1fa52990c7836d72e8d70cd7753f2362c72fbb0a49c1462e8c60e7176d0b/rpds_py-0.23.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:c8f7e90b948dc9dcfff8003f1ea3af08b29c062f681c05fd798e36daa3f7e3e8", size = 561792 },
    { url = "https://files.pythonhosted.org/packages/57/b8/fe3b612979b1a29d0c77f8585903d8b3a292604b26d4b300e228b8ac6360/rpds_py-0.23.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:5b98b6c953e5c2bda51ab4d5b4f172617d462eebc7f4bfdc7c7e6b423f6da957", size = 588127 },
    { url = "https://files.pythonhosted.org/packages/44/2d/fde474de516bbc4b9b230f43c98e7f8acc5da7fc50ceed8e7af27553d346/rpds_py-0.23.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:2893d778d4671ee627bac4037a075168b2673c57186fb1a57e993465dbd79a93", size = 556981 },
    { url = "https://files.pythonhosted.org/packages/18/57/767deeb27b81370bbab8f74ef6e68d26c4ea99018f3c71a570e506fede85/rpds_py-0.23.1-cp313-cp313-win32.whl", hash = "sha256:2cfa07c346a7ad07019c33fb9a63cf3acb1f5363c33bc73014e20d9fe8b01cdd", size = 221936 },
    { url = "https://files.pythonhosted.org/packages/7d/6c/3474cfdd3cafe243f97ab8474ea8949236eb2a1a341ca55e75ce00cd03da/rpds_py-0.23.1-cp313-cp313-win_amd64.whl", hash = "sha256:3aaf141d39f45322e44fc2c742e4b8b4098ead5317e5f884770c8df0c332da70", size = 237145 },
    { url = "https://files.pythonhosted.org/packages/ec/77/e985064c624230f61efa0423759bb066da56ebe40c654f8b5ba225bd5d63/rpds_py-0.23.1-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:759462b2d0aa5a04be5b3e37fb8183615f47014ae6b116e17036b131985cb731", size = 359623 },
    { url = "https://files.pythonhosted.org/packages/62/d9/a33dcbf62b29e40559e012d525bae7d516757cf042cc9234bd34ca4b6aeb/rpds_py-0.23.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3e9212f52074fc9d72cf242a84063787ab8e21e0950d4d6709886fb62bcb91d5", size = 345900 },
    { url = "https://files.pythonhosted.org/packages/92/eb/f81a4be6397861adb2cb868bb6a28a33292c2dcac567d1dc575226055e55/rpds_py-0.23.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9e9f3a3ac919406bc0414bbbd76c6af99253c507150191ea79fab42fdb35982a", size = 386426 },
    { url = "https://files.pythonhosted.org/packages/09/47/1f810c9b5e83be005341201b5389f1d240dfa440346ea7189f9b3fd6961d/rpds_py-0.23.1-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:c04ca91dda8a61584165825907f5c967ca09e9c65fe8966ee753a3f2b019fe1e", size = 392314 },
    { url = "https://files.pythonhosted.org/packages/83/bd/bc95831432fd6c46ed8001f01af26de0763a059d6d7e6d69e3c5bf02917a/rpds_py-0.23.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4ab923167cfd945abb9b51a407407cf19f5bee35001221f2911dc85ffd35ff4f", size = 447706 },
    { url = "https://files.pythonhosted.org/packages/19/3e/567c04c226b1802dc6dc82cad3d53e1fa0a773258571c74ac5d8fbde97ed/rpds_py-0.23.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed6f011bedca8585787e5082cce081bac3d30f54520097b2411351b3574e1219", size = 437060 },
    { url = "https://files.pythonhosted.org/packages/fe/77/a77d2c6afe27ae7d0d55fc32f6841502648070dc8d549fcc1e6d47ff8975/rpds_py-0.23.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6959bb9928c5c999aba4a3f5a6799d571ddc2c59ff49917ecf55be2bbb4e3722", size = 389347 },
    { url = "https://files.pythonhosted.org/packages/3f/47/6b256ff20a74cfebeac790ab05586e0ac91f88e331125d4740a6c86fc26f/rpds_py-0.23.1-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1ed7de3c86721b4e83ac440751329ec6a1102229aa18163f84c75b06b525ad7e", size = 415554 },
    { url = "https://files.pythonhosted.org/packages/fc/29/d4572469a245bc9fc81e35166dca19fc5298d5c43e1a6dd64bf145045193/rpds_py-0.23.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:5fb89edee2fa237584e532fbf78f0ddd1e49a47c7c8cfa153ab4849dc72a35e6", size = 557418 },
    { url = "https://files.pythonhosted.org/packages/9c/0a/68cf7228895b1a3f6f39f51b15830e62456795e61193d2c8b87fd48c60db/rpds_py-0.23.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:7e5413d2e2d86025e73f05510ad23dad5950ab8417b7fc6beaad99be8077138b", size = 583033 },
    { url = "https://files.pythonhosted.org/packages/14/18/017ab41dcd6649ad5db7d00155b4c212b31ab05bd857d5ba73a1617984eb/rpds_py-0.23.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:d31ed4987d72aabdf521eddfb6a72988703c091cfc0064330b9e5f8d6a042ff5", size = 554880 },
    { url = "https://files.pythonhosted.org/packages/2e/dd/17de89431268da8819d8d51ce67beac28d9b22fccf437bc5d6d2bcd1acdb/rpds_py-0.23.1-cp313-cp313t-win32.whl", hash = "sha256:f3429fb8e15b20961efca8c8b21432623d85db2228cc73fe22756c6637aa39e7", size = 219743 },
    { url = "https://files.pythonhosted.org/packages/68/15/6d22d07e063ce5e9bfbd96db9ec2fbb4693591b4503e3a76996639474d02/rpds_py-0.23.1-cp313-cp313t-win_amd64.whl", hash = "sha256:d6f6512a90bd5cd9030a6237f5346f046c6f0e40af98657568fa45695d4de59d", size = 235415 },
]

[[package]]
name = "six"
version = "1.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/e7/b2c673351809dca68a0e064b6af791aa332cf192da575fd474ed7d6f16a2/six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81", size = 34031 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274", size = 11050 },
]

[[package]]
name = "smmap"
version = "5.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/44/cd/a040c4b3119bbe532e5b0732286f805445375489fceaec1f48306068ee3b/smmap-5.0.2.tar.gz", hash = "sha256:26ea65a03958fa0c8a1c7e8c7a58fdc77221b8910f6be2131affade476898ad5", size = 22329 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/be/d09147ad1ec7934636ad912901c5fd7667e1c858e19d355237db0d0cd5e4/smmap-5.0.2-py3-none-any.whl", hash = "sha256:b30115f0def7d7531d22a0fb6502488d879e75b260a9db4d0819cfb25403af5e", size = 24303 },
]

[[package]]
name = "sqlalchemy"
version = "2.0.38"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "greenlet", marker = "(python_full_version < '3.14' and platform_machine == 'AMD64') or (python_full_version < '3.14' and platform_machine == 'WIN32') or (python_full_version < '3.14' and platform_machine == 'aarch64') or (python_full_version < '3.14' and platform_machine == 'amd64') or (python_full_version < '3.14' and platform_machine == 'ppc64le') or (python_full_version < '3.14' and platform_machine == 'win32') or (python_full_version < '3.14' and platform_machine == 'x86_64')" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e4/08/9a90962ea72acd532bda71249a626344d855c4032603924b1b547694b837/sqlalchemy-2.0.38.tar.gz", hash = "sha256:e5a4d82bdb4bf1ac1285a68eab02d253ab73355d9f0fe725a97e1e0fa689decb", size = 9634782 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/6c/9d3a638f297fce288ba12a4e5dbd08ef1841d119abee9300c100eba00217/SQLAlchemy-2.0.38-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:bf89e0e4a30714b357f5d46b6f20e0099d38b30d45fa68ea48589faf5f12f62d", size = 2106330 },
    { url = "https://files.pythonhosted.org/packages/0e/57/d5fdee56f418491267701965795805662b1744de40915d4764451390536d/SQLAlchemy-2.0.38-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8455aa60da49cb112df62b4721bd8ad3654a3a02b9452c783e651637a1f21fa2", size = 2096730 },
    { url = "https://files.pythonhosted.org/packages/42/84/205f423f8b28329c47237b7e130a7f93c234a49fab20b4534bd1ff26a06a/SQLAlchemy-2.0.38-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f53c0d6a859b2db58332e0e6a921582a02c1677cc93d4cbb36fdf49709b327b2", size = 3215023 },
    { url = "https://files.pythonhosted.org/packages/77/41/94a558d47bffae5a361b0cfb3721324ea4154829dd5432f80bd4cfeecbc9/SQLAlchemy-2.0.38-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b3c4817dff8cef5697f5afe5fec6bc1783994d55a68391be24cb7d80d2dbc3a6", size = 3214991 },
    { url = "https://files.pythonhosted.org/packages/74/a0/cc3c030e7440bd17ce67c1875f50edb41d0ef17b9c76fbc290ef27bbe37f/SQLAlchemy-2.0.38-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c9cea5b756173bb86e2235f2f871b406a9b9d722417ae31e5391ccaef5348f2c", size = 3151854 },
    { url = "https://files.pythonhosted.org/packages/24/ab/8ba2588c2eb1d092944551354d775ef4fc0250badede324d786a4395d10e/SQLAlchemy-2.0.38-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:40e9cdbd18c1f84631312b64993f7d755d85a3930252f6276a77432a2b25a2f3", size = 3172158 },
    { url = "https://files.pythonhosted.org/packages/e0/73/2a3d6217e8e6abb553ed410ce5adc0bdec7effd684716f0fbaee5831d677/SQLAlchemy-2.0.38-cp311-cp311-win32.whl", hash = "sha256:cb39ed598aaf102251483f3e4675c5dd6b289c8142210ef76ba24aae0a8f8aba", size = 2076965 },
    { url = "https://files.pythonhosted.org/packages/a4/17/364a99c8c5698492c7fa40fc463bf388f05b0b03b74028828b71a79dc89d/SQLAlchemy-2.0.38-cp311-cp311-win_amd64.whl", hash = "sha256:f9d57f1b3061b3e21476b0ad5f0397b112b94ace21d1f439f2db472e568178ae", size = 2102169 },
    { url = "https://files.pythonhosted.org/packages/5a/f8/6d0424af1442c989b655a7b5f608bc2ae5e4f94cdf6df9f6054f629dc587/SQLAlchemy-2.0.38-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:12d5b06a1f3aeccf295a5843c86835033797fea292c60e72b07bcb5d820e6dd3", size = 2104927 },
    { url = "https://files.pythonhosted.org/packages/25/80/fc06e65fca0a19533e2bfab633a5633ed8b6ee0b9c8d580acf84609ce4da/SQLAlchemy-2.0.38-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:e036549ad14f2b414c725349cce0772ea34a7ab008e9cd67f9084e4f371d1f32", size = 2095317 },
    { url = "https://files.pythonhosted.org/packages/98/2d/5d66605f76b8e344813237dc160a01f03b987201e974b46056a7fb94a874/SQLAlchemy-2.0.38-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ee3bee874cb1fadee2ff2b79fc9fc808aa638670f28b2145074538d4a6a5028e", size = 3244735 },
    { url = "https://files.pythonhosted.org/packages/73/8d/b0539e8dce90861efc38fea3eefb15a5d0cfeacf818614762e77a9f192f9/SQLAlchemy-2.0.38-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e185ea07a99ce8b8edfc788c586c538c4b1351007e614ceb708fd01b095ef33e", size = 3255581 },
    { url = "https://files.pythonhosted.org/packages/ac/a5/94e1e44bf5bdffd1782807fcc072542b110b950f0be53f49e68b5f5eca1b/SQLAlchemy-2.0.38-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b79ee64d01d05a5476d5cceb3c27b5535e6bb84ee0f872ba60d9a8cd4d0e6579", size = 3190877 },
    { url = "https://files.pythonhosted.org/packages/91/13/f08b09996dce945aec029c64f61c13b4788541ac588d9288e31e0d3d8850/SQLAlchemy-2.0.38-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:afd776cf1ebfc7f9aa42a09cf19feadb40a26366802d86c1fba080d8e5e74bdd", size = 3217485 },
    { url = "https://files.pythonhosted.org/packages/13/8f/8cfe2ba5ba6d8090f4de0e658330c53be6b7bf430a8df1b141c2b180dcdf/SQLAlchemy-2.0.38-cp312-cp312-win32.whl", hash = "sha256:a5645cd45f56895cfe3ca3459aed9ff2d3f9aaa29ff7edf557fa7a23515a3725", size = 2075254 },
    { url = "https://files.pythonhosted.org/packages/c2/5c/e3c77fae41862be1da966ca98eec7fbc07cdd0b00f8b3e1ef2a13eaa6cca/SQLAlchemy-2.0.38-cp312-cp312-win_amd64.whl", hash = "sha256:1052723e6cd95312f6a6eff9a279fd41bbae67633415373fdac3c430eca3425d", size = 2100865 },
    { url = "https://files.pythonhosted.org/packages/21/77/caa875a1f5a8a8980b564cc0e6fee1bc992d62d29101252561d0a5e9719c/SQLAlchemy-2.0.38-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ecef029b69843b82048c5b347d8e6049356aa24ed644006c9a9d7098c3bd3bfd", size = 2100201 },
    { url = "https://files.pythonhosted.org/packages/f4/ec/94bb036ec78bf9a20f8010c807105da9152dd84f72e8c51681ad2f30b3fd/SQLAlchemy-2.0.38-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9c8bcad7fc12f0cc5896d8e10fdf703c45bd487294a986903fe032c72201596b", size = 2090678 },
    { url = "https://files.pythonhosted.org/packages/7b/61/63ff1893f146e34d3934c0860209fdd3925c25ee064330e6c2152bacc335/SQLAlchemy-2.0.38-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2a0ef3f98175d77180ffdc623d38e9f1736e8d86b6ba70bff182a7e68bed7727", size = 3177107 },
    { url = "https://files.pythonhosted.org/packages/a9/4f/b933bea41a602b5f274065cc824fae25780ed38664d735575192490a021b/SQLAlchemy-2.0.38-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8b0ac78898c50e2574e9f938d2e5caa8fe187d7a5b69b65faa1ea4648925b096", size = 3190435 },
    { url = "https://files.pythonhosted.org/packages/f5/23/9e654b4059e385988de08c5d3b38a369ea042f4c4d7c8902376fd737096a/SQLAlchemy-2.0.38-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:9eb4fa13c8c7a2404b6a8e3772c17a55b1ba18bc711e25e4d6c0c9f5f541b02a", size = 3123648 },
    { url = "https://files.pythonhosted.org/packages/83/59/94c6d804e76ebc6412a08d2b086a8cb3e5a056cd61508e18ddaf3ec70100/SQLAlchemy-2.0.38-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5dba1cdb8f319084f5b00d41207b2079822aa8d6a4667c0f369fce85e34b0c86", size = 3151789 },
    { url = "https://files.pythonhosted.org/packages/b2/27/17f143013aabbe1256dce19061eafdce0b0142465ce32168cdb9a18c04b1/SQLAlchemy-2.0.38-cp313-cp313-win32.whl", hash = "sha256:eae27ad7580529a427cfdd52c87abb2dfb15ce2b7a3e0fc29fbb63e2ed6f8120", size = 2073023 },
    { url = "https://files.pythonhosted.org/packages/e2/3e/259404b03c3ed2e7eee4c179e001a07d9b61070334be91124cf4ad32eec7/SQLAlchemy-2.0.38-cp313-cp313-win_amd64.whl", hash = "sha256:b335a7c958bc945e10c522c069cd6e5804f4ff20f9a744dd38e748eb602cbbda", size = 2096908 },
    { url = "https://files.pythonhosted.org/packages/aa/e4/592120713a314621c692211eba034d09becaf6bc8848fabc1dc2a54d8c16/SQLAlchemy-2.0.38-py3-none-any.whl", hash = "sha256:63178c675d4c80def39f1febd625a6333f44c0ba269edd8a468b156394b27753", size = 1896347 },
]

[[package]]
name = "streamlit"
version = "1.42.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "altair" },
    { name = "blinker" },
    { name = "cachetools" },
    { name = "click" },
    { name = "gitpython" },
    { name = "numpy" },
    { name = "packaging" },
    { name = "pandas" },
    { name = "pillow" },
    { name = "protobuf" },
    { name = "pyarrow" },
    { name = "pydeck" },
    { name = "requests" },
    { name = "rich" },
    { name = "tenacity" },
    { name = "toml" },
    { name = "tornado" },
    { name = "typing-extensions" },
    { name = "watchdog", marker = "sys_platform != 'darwin'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/08/58/b1875ccb6901cec7a721059bfd9122107d29e0b0ccfdcea9d353af6b5c52/streamlit-1.42.2.tar.gz", hash = "sha256:62026dbdcb482790933f658b096d7dd58fa70da89c1f06fbc3658b91dcd4dab2", size = 9169615 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e4/08/c962e38f4450dafb98af49f8988a736dd67ae9cc26a5704c43269f506bc8/streamlit-1.42.2-py2.py3-none-any.whl", hash = "sha256:e2516c7fcd17a11a85cc1999fae58ace0a6458e2b4c1a411ed3d75b1aee2eb93", size = 9559800 },
]

[[package]]
name = "tenacity"
version = "9.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/cd/94/91fccdb4b8110642462e653d5dcb27e7b674742ad68efd146367da7bdb10/tenacity-9.0.0.tar.gz", hash = "sha256:807f37ca97d62aa361264d497b0e31e92b8027044942bfa756160d908320d73b", size = 47421 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b6/cb/b86984bed139586d01532a587464b5805f12e397594f19f931c4c2fbfa61/tenacity-9.0.0-py3-none-any.whl", hash = "sha256:93de0c98785b27fcf659856aa9f54bfbd399e29969b0621bc7f762bd441b4539", size = 28169 },
]

[[package]]
name = "toml"
version = "0.10.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/be/ba/1f744cdc819428fc6b5084ec34d9b30660f6f9daaf70eead706e3203ec3c/toml-0.10.2.tar.gz", hash = "sha256:b3bda1d108d5dd99f4a20d24d9c348e91c4db7ab1b749200bded2f839ccbe68f", size = 22253 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/44/6f/7120676b6d73228c96e17f1f794d8ab046fc910d781c8d151120c3f1569e/toml-0.10.2-py2.py3-none-any.whl", hash = "sha256:806143ae5bfb6a3c6e736a764057db0e6a0e05e338b5630894a5f779cabb4f9b", size = 16588 },
]

[[package]]
name = "tornado"
version = "6.4.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/59/45/a0daf161f7d6f36c3ea5fc0c2de619746cc3dd4c76402e9db545bd920f63/tornado-6.4.2.tar.gz", hash = "sha256:92bad5b4746e9879fd7bf1eb21dce4e3fc5128d71601f80005afa39237ad620b", size = 501135 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/26/7e/71f604d8cea1b58f82ba3590290b66da1e72d840aeb37e0d5f7291bd30db/tornado-6.4.2-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:e828cce1123e9e44ae2a50a9de3055497ab1d0aeb440c5ac23064d9e44880da1", size = 436299 },
    { url = "https://files.pythonhosted.org/packages/96/44/87543a3b99016d0bf54fdaab30d24bf0af2e848f1d13d34a3a5380aabe16/tornado-6.4.2-cp38-abi3-macosx_10_9_x86_64.whl", hash = "sha256:072ce12ada169c5b00b7d92a99ba089447ccc993ea2143c9ede887e0937aa803", size = 434253 },
    { url = "https://files.pythonhosted.org/packages/cb/fb/fdf679b4ce51bcb7210801ef4f11fdac96e9885daa402861751353beea6e/tornado-6.4.2-cp38-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1a017d239bd1bb0919f72af256a970624241f070496635784d9bf0db640d3fec", size = 437602 },
    { url = "https://files.pythonhosted.org/packages/4f/3b/e31aeffffc22b475a64dbeb273026a21b5b566f74dee48742817626c47dc/tornado-6.4.2-cp38-abi3-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c36e62ce8f63409301537222faffcef7dfc5284f27eec227389f2ad11b09d946", size = 436972 },
    { url = "https://files.pythonhosted.org/packages/22/55/b78a464de78051a30599ceb6983b01d8f732e6f69bf37b4ed07f642ac0fc/tornado-6.4.2-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bca9eb02196e789c9cb5c3c7c0f04fb447dc2adffd95265b2c7223a8a615ccbf", size = 437173 },
    { url = "https://files.pythonhosted.org/packages/79/5e/be4fb0d1684eb822c9a62fb18a3e44a06188f78aa466b2ad991d2ee31104/tornado-6.4.2-cp38-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:304463bd0772442ff4d0f5149c6f1c2135a1fae045adf070821c6cdc76980634", size = 437892 },
    { url = "https://files.pythonhosted.org/packages/f5/33/4f91fdd94ea36e1d796147003b490fe60a0215ac5737b6f9c65e160d4fe0/tornado-6.4.2-cp38-abi3-musllinux_1_2_i686.whl", hash = "sha256:c82c46813ba483a385ab2a99caeaedf92585a1f90defb5693351fa7e4ea0bf73", size = 437334 },
    { url = "https://files.pythonhosted.org/packages/2b/ae/c1b22d4524b0e10da2f29a176fb2890386f7bd1f63aacf186444873a88a0/tornado-6.4.2-cp38-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:932d195ca9015956fa502c6b56af9eb06106140d844a335590c1ec7f5277d10c", size = 437261 },
    { url = "https://files.pythonhosted.org/packages/b5/25/36dbd49ab6d179bcfc4c6c093a51795a4f3bed380543a8242ac3517a1751/tornado-6.4.2-cp38-abi3-win32.whl", hash = "sha256:2876cef82e6c5978fde1e0d5b1f919d756968d5b4282418f3146b79b58556482", size = 438463 },
    { url = "https://files.pythonhosted.org/packages/61/cc/58b1adeb1bb46228442081e746fcdbc4540905c87e8add7c277540934edb/tornado-6.4.2-cp38-abi3-win_amd64.whl", hash = "sha256:908b71bf3ff37d81073356a5fadcc660eb10c1476ee6e2725588626ce7e5ca38", size = 438907 },
]

[[package]]
name = "typing-extensions"
version = "4.12.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/df/db/f35a00659bc03fec321ba8bce9420de607a1d37f8342eee1863174c69557/typing_extensions-4.12.2.tar.gz", hash = "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8", size = 85321 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/26/9f/ad63fc0248c5379346306f8668cda6e2e2e9c95e01216d2b8ffd9ff037d0/typing_extensions-4.12.2-py3-none-any.whl", hash = "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d", size = 37438 },
]

[[package]]
name = "tzdata"
version = "2025.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/43/0f/fa4723f22942480be4ca9527bbde8d43f6c3f2fe8412f00e7f5f6746bc8b/tzdata-2025.1.tar.gz", hash = "sha256:24894909e88cdb28bd1636c6887801df64cb485bd593f2fd83ef29075a81d694", size = 194950 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0f/dd/84f10e23edd882c6f968c21c2434fe67bd4a528967067515feca9e611e5e/tzdata-2025.1-py2.py3-none-any.whl", hash = "sha256:7e127113816800496f027041c570f50bcd464a020098a3b6b199517772303639", size = 346762 },
]

[[package]]
name = "urllib3"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/aa/63/e53da845320b757bf29ef6a9062f5c669fe997973f966045cb019c3f4b66/urllib3-2.3.0.tar.gz", hash = "sha256:f8c5449b3cf0861679ce7e0503c7b44b5ec981bec0d1d3795a07f1ba96f0204d", size = 307268 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c8/19/4ec628951a74043532ca2cf5d97b7b14863931476d117c471e8e2b1eb39f/urllib3-2.3.0-py3-none-any.whl", hash = "sha256:1cee9ad369867bfdbbb48b7dd50374c0967a0bb7710050facf0dd6911440e3df", size = 128369 },
]

[[package]]
name = "watchdog"
version = "6.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/db/7d/7f3d619e951c88ed75c6037b246ddcf2d322812ee8ea189be89511721d54/watchdog-6.0.0.tar.gz", hash = "sha256:9ddf7c82fda3ae8e24decda1338ede66e1c99883db93711d8fb941eaa2d8c282", size = 131220 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a9/c7/ca4bf3e518cb57a686b2feb4f55a1892fd9a3dd13f470fca14e00f80ea36/watchdog-6.0.0-py3-none-manylinux2014_aarch64.whl", hash = "sha256:7607498efa04a3542ae3e05e64da8202e58159aa1fa4acddf7678d34a35d4f13", size = 79079 },
    { url = "https://files.pythonhosted.org/packages/5c/51/d46dc9332f9a647593c947b4b88e2381c8dfc0942d15b8edc0310fa4abb1/watchdog-6.0.0-py3-none-manylinux2014_armv7l.whl", hash = "sha256:9041567ee8953024c83343288ccc458fd0a2d811d6a0fd68c4c22609e3490379", size = 79078 },
    { url = "https://files.pythonhosted.org/packages/d4/57/04edbf5e169cd318d5f07b4766fee38e825d64b6913ca157ca32d1a42267/watchdog-6.0.0-py3-none-manylinux2014_i686.whl", hash = "sha256:82dc3e3143c7e38ec49d61af98d6558288c415eac98486a5c581726e0737c00e", size = 79076 },
    { url = "https://files.pythonhosted.org/packages/ab/cc/da8422b300e13cb187d2203f20b9253e91058aaf7db65b74142013478e66/watchdog-6.0.0-py3-none-manylinux2014_ppc64.whl", hash = "sha256:212ac9b8bf1161dc91bd09c048048a95ca3a4c4f5e5d4a7d1b1a7d5752a7f96f", size = 79077 },
    { url = "https://files.pythonhosted.org/packages/2c/3b/b8964e04ae1a025c44ba8e4291f86e97fac443bca31de8bd98d3263d2fcf/watchdog-6.0.0-py3-none-manylinux2014_ppc64le.whl", hash = "sha256:e3df4cbb9a450c6d49318f6d14f4bbc80d763fa587ba46ec86f99f9e6876bb26", size = 79078 },
    { url = "https://files.pythonhosted.org/packages/62/ae/a696eb424bedff7407801c257d4b1afda455fe40821a2be430e173660e81/watchdog-6.0.0-py3-none-manylinux2014_s390x.whl", hash = "sha256:2cce7cfc2008eb51feb6aab51251fd79b85d9894e98ba847408f662b3395ca3c", size = 79077 },
    { url = "https://files.pythonhosted.org/packages/b5/e8/dbf020b4d98251a9860752a094d09a65e1b436ad181faf929983f697048f/watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl", hash = "sha256:20ffe5b202af80ab4266dcd3e91aae72bf2da48c0d33bdb15c66658e685e94e2", size = 79078 },
    { url = "https://files.pythonhosted.org/packages/07/f6/d0e5b343768e8bcb4cda79f0f2f55051bf26177ecd5651f84c07567461cf/watchdog-6.0.0-py3-none-win32.whl", hash = "sha256:07df1fdd701c5d4c8e55ef6cf55b8f0120fe1aef7ef39a1c6fc6bc2e606d517a", size = 79065 },
    { url = "https://files.pythonhosted.org/packages/db/d9/c495884c6e548fce18a8f40568ff120bc3a4b7b99813081c8ac0c936fa64/watchdog-6.0.0-py3-none-win_amd64.whl", hash = "sha256:cbafb470cf848d93b5d013e2ecb245d4aa1c8fd0504e863ccefa32445359d680", size = 79070 },
    { url = "https://files.pythonhosted.org/packages/33/e8/e40370e6d74ddba47f002a32919d91310d6074130fe4e17dabcafc15cbf1/watchdog-6.0.0-py3-none-win_ia64.whl", hash = "sha256:a1914259fa9e1454315171103c6a30961236f508b9b623eae470268bbcc6a22f", size = 79067 },
]
