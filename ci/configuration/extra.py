PLUGINS = ['netbox_licensing']
DEBUG = True
SECRET_KEY = 'dummydummydummydummydummydummydummydummydummydummy'
DEVELOPER = True
PLUGINS_CONFIG = {
    'netbox_licensing': dict(
        TEST_RUNNER='xmlrunner.extra.djangotestrunner.XMLTestRunner',
        TEST_OUTPUT_DIR='/ci/reports/',
        TEST_OUTPUT_FILE_NAME='junit.xml',
    )
}
