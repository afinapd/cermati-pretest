validEmail = [
    {
        'email': 'email@example.com',
    },
    {
        'email': 'firstname.lastname@example.com',
    },
    {
        'email': 'email@subdomain.example.com',
    },
    {
        'email': 'firstname+lastname@example.com',
    },
    {
        'email': "'email'@example.com",
    },
    {
        'email': '1234567890@example.com',
    },
    {
        'email': 'email@example-one.com',
    },
    {
        'email': '_______@example.com',
    },
    {
        'email': 'email@example.museum',
    },
    {
        'email': 'email@example.co.jp',
    },
    {
        'email': 'firstname-lastname@example.com',
    },
    {
        'email': 'email@example.name',
    }
]

invalidEmail = [
    {
        'email': '',
        'alertMessage': 'Input ini wajib diisi.'
    },
    {
        'email': 'email@123.123.123.123',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email@[123.123.123.123]',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'plainaddress',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': '#@%^%#$@#$@#.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': '@example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'Joe Smith <email@example.com>',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email.example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email@example@example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': '.email@example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email.@example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email..email@example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email@example.com (Joe Smith)',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email@example',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email@-example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'email@example..com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'Abc..123@example.com',
        'alertMessage': 'Format email tidak valid.'
    },
    {
        'email': 'test3',
        'alertMessage': 'Format email tidak valid.'
    }
]

validPassword = [
    {
        'password': 'test1234',
    }
]

invalidPassword = [
    {
        'password': '',
        'alertMessage': 'Input ini wajib diisi.'
    },
    {
        'password': 't1...',
        'alertMessage': 'Password harus memiliki panjang antara 8 - 50 karakter dan mengandung 1 huruf dan 1 angka',
    },
    {
        'password': 'abcdefghyy',
        'alertMessage': 'Password harus memiliki panjang antara 8 - 50 karakter dan mengandung 1 huruf dan 1 angka',
    },
    {
        'password': '12345678',
        'alertMessage': 'Password harus memiliki panjang antara 8 - 50 karakter dan mengandung 1 huruf dan 1 angka',
    },
    {
        'password': '..............',
        'alertMessage': 'Password harus memiliki panjang antara 8 - 50 karakter dan mengandung 1 huruf dan 1 angka',
    },
    {
        'password': '1234....',
        'alertMessage': 'Password harus memiliki panjang antara 8 - 50 karakter dan mengandung 1 huruf dan 1 angka',
    },
    {
        'password': 'test.......',
        'alertMessage': 'Password harus memiliki panjang antara 8 - 50 karakter dan mengandung 1 huruf dan 1 angka',
    }
]

invalidConfirmPassword = [
    {
        'password': '',
        'alertMessage': 'Input ini wajib diisi.'
    },
    {
        'password': 't1...',
        'alertMessage': 'Kata Sandi tidak sama dengan Konfirmasi Kata Sandi',
    },
    {
        'password': 'abcdefghyy',
        'alertMessage': 'Kata Sandi tidak sama dengan Konfirmasi Kata Sandi',
    },
    {
        'password': '12345678',
        'alertMessage': 'Kata Sandi tidak sama dengan Konfirmasi Kata Sandi',
    },
    {
        'password': '..............',
        'alertMessage': 'Kata Sandi tidak sama dengan Konfirmasi Kata Sandi',
    },
    {
        'password': '1234....',
        'alertMessage': 'Kata Sandi tidak sama dengan Konfirmasi Kata Sandi',
    },
    {
        'password': 'test.......',
        'alertMessage': 'Kata Sandi tidak sama dengan Konfirmasi Kata Sandi',
    }
]

validName = [
    {
        'name': 'Afina',
    },
    {
        'name': 'afina.',
    },
    {
        'name': 'afina,',
    },
    {
        'name': 'afina-',
    },
    {
        'name': "afina'",
    }
]

invalidName = [
    {
        'name': '',
        'alertMessage': 'Input ini wajib diisi.'
    },
    {
        'name': '09298918',
        'alertMessage': "Nama hanya dapat diisi dengan karakter alfabet, titik (.), petik ('), koma (,), strip (-) dan spasi."
    },
    {
        'name': '...........',
        'alertMessage': "Nama hanya dapat diisi dengan karakter alfabet, titik (.), petik ('), koma (,), strip (-) dan spasi."
    },
    {
        'name': ',,,,,,,,,,,,,,',
        'alertMessage': "Nama hanya dapat diisi dengan karakter alfabet, titik (.), petik ('), koma (,), strip (-) dan spasi."
    },
    {
        'name': '---------------',
        'alertMessage': "Nama hanya dapat diisi dengan karakter alfabet, titik (.), petik ('), koma (,), strip (-) dan spasi."
    },
    {
        'name': "''''''''''''''",
        'alertMessage': "Nama hanya dapat diisi dengan karakter alfabet, titik (.), petik ('), koma (,), strip (-) dan spasi."
    },
    {
        'name': 'A/////-1-1-ina',
        'alertMessage': "Nama hanya dapat diisi dengan karakter alfabet, titik (.), petik ('), koma (,), strip (-) dan spasi."
    }
]

validMobilePhone = [
    {
        'mobilePhone': '0857726100',
    },
    {
        'mobilePhone': '0857726100273',
    }
]

invalidMobilePhone = [
    {
        'mobilePhone': '',
        'alertMessage': 'Input ini wajib diisi.'
    },
    {
        'mobilePhone': '85712610027',
        'alertMessage': 'Nomor telepon tidak valid.',
    },
    {
        'mobilePhone': '0857726',
        'alertMessage': 'Nomor telepon tidak valid.',
    },
    {
        'mobilePhone': '88800273',
        'alertMessage': 'Nomor telepon tidak valid.',
    }
]