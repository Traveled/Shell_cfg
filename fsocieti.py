#! /usr/bin/env python
import base64
print base64.b64decode("CiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQEBAIzogICAgICAgK0BAQEBAQCAsQEBAQEBAQEBAQEBAIzogICAgICAgICAgICAgICAgICAgQEBAQEBAQEBAQEBAQCtgICAgICAgICAgYCtAQEBAQEBAIzogICAgIC5AQEBAQEBAQEBAJyAgICAgICAgICA6K0BAQEBAQEArLiAgICAgI0BAQEBAQEBAQEBAQEBAQEBAQAogICAgICAgICAgICAgICAgICAgICAgICdAQEBAQEBAQCAgICAsQEBAQEBAQEAgLEBAQEBAQEBAQEBAQEBAQGAgICAgICAgICAgICAgICAgIEBAQEBAQEBAQEBAQEBAQEAgICAgICAgQEBAQEBAQEBAQEBAQCwgICAsQEBAQEBAQEBAQEBAJyAgICAgIC5AQEBAQEBAQEBAQEBAICAgIEBAQEBAQEBAQEBAQEBAQEBAQEAKICAgICAgICAgICAgICAgICAgICAgICAnQEBAQEBAQEAsICAgQEBAQEBAQEBAICxAQEBAQEBAQEBAQEBAQEBALiAgICAgICAgICAgICAgICBAQEBAQEBAQEBAQEBAQEBAQCAgICAgQEBAQEBAQEBAQEBAQEBALCAgLEBAQEBAQEBAQEBAQEAjICAgIGBAQEBAQEBAQEBAQEBAQEAgICBAQEBAQEBAQEBAQEBAQEBAQEBACiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQCwnQEBAQCAgK0BAQCs6O0BAQCBgLCwsLCwsLCwsLDo6I0BAQEBgICAgICAgICAgICAgICAgLCwsLCwsLCwsLCwsJ0BAQEBAICAgK0BAQEAnLCwsLCwnI0BAQEAgIGAsLCwsLCwsLCwnQEBAQDsgICBAQEBAQCcsLCwsLCdAQEBAIyAgLCwsLCwsLCw6LCwsLCwsLCwsLAogICAgICAgICAgICAgICAgICAgICAgICdAQEAuOi5AQEA6IEBAQCsgI2BAQEAgLCMjIyMjIyMjIyMjIywsQEBAIyAgICAgICAgICAgICAgICMjIyMjIyMjIyMjIysgI0BAQCwgIEBAQEAgOyMjIyMjK2AnQEBALiAuIyMjIyMjIyMjJyBAQEBAICBgQEBAJyArIyMjIyMnIEBAQEAgICMjIyMjIyMjI2AjIyMjIyMjIyMKICAgICAgICAgICAgICAgICAgICAgICAnQEBALEAgQEBAQCNAQEAgI0BgQEBAICxAQEBAQEBAQEBAQEBAJyxAQEAgICAgICAgICAgICAgICBAQEBAQEBAQEBAQEBAQCBAQEBAIGBAQEAgQEBAQEBAQEBAIEBAQCsgLEBAQEBAQEBAQEBAIEBAQCcgOkBAQCBAQEBAQEBAQEAgQEBAYCBAQEBAQEBAQEBgQEBAQEBAQEBACiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQDpAOi5AQEBAQEBAIEBAYEBAQCAsQEBAQEBAQEBAQEBAQEAgQEBAOiAgICAgICAgICAgICAgQEBAQEBAQEBAQEBAQEAjOkBAQCAuQEBAIEBAQEBAQEBAQDsrQEAjICxAQEBAQEBAQEBAQCwrQEBAICNAQEAsQEBAQEBAQEBAIEBAQDsgQEBAQEBAQEBAYEBAQEBAQEBAQAogICAgICAgICAgICAgICAgICAgICAgICdAQEA6QEAgQEBAQEBAYCdAQGBAQEAgYCwsLCwsLCwsLCwnQEBALEBAQEAgICAgICAgICAgICAgIDo6JycnJywsLCc7I0BAQCBAQEAgLEBAQGBAQEArOjpAQEAjO0BAQCAsQEAnOicnJydAQEBALEBAQCAjQEAjJ0BAQCsnK0BAQGBAQEA7IDosLCwsOkBAQGBAQEAjOyw6JycKICAgICAgICAgICAgICAgICAgICAgICAnQEBAOkBALixAQEBAIyBAQEBgQEBAIC4jIysjIyMrKyMjI0BAQCxAQEAjICAgICAgICAgICAgICArIyMjIyMjIyMrI0BAQEAgQEBAICxAQEBgQEBAICAgI0BAIydAQEAgLkBAKysrKysrQEBAQCxAQEAgI0BAIydAQEAgICBAQEBgQEBAOyAgICAgICBAQEBgQEBALAogICAgICAgICAgICAgICAgICAgICAgICdAQEA6QEBAIEBAQEAgO0BAQGBAQEAgLEBAQEBAQEBAQEBAQEBAIEBAQDsgICAgICAgICAgICAgIEBAQEBAQEBAQEBAQEBAIyxAQEAgLEBAQGBAQEAgICAjQEAjJ0BAQCAsQEBAQEBAQEBAQEAsK0BAQCAjQEAjJ0BAQCAgIEBAQGBAQEA7ICAgICAgIEBAQGBAQEAsCiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQDpAQEAuO0BAQCBAQEBAYEBAQCAsQEBAQEBAQEBAQEBAQDo7QEBAYCAgICAgICAgICAgICAgQEBAQEBAQEBAQEBAQEAgQEBAQCAsQEBAYEBAQCAgICNAQCMnQEBAICxAQEBAQEBAQEBAQCBAQEAnIEBAQCMnQEBAICAgQEBAYEBAQDsgICAgICAgQEBAYEBAQCwKICAgICAgICAgICAgICAgICAgICAgICAnQEBAOkBAQCMgQEAsLEBAQEBgQEBAICxAQEAjIyMjIyMjIyNgOkBAQEAgICAgICAgICAgICAgICBAQEBAIyMjIyMjIyMnIEBAQEA6ICxAQEBgQEBAICAgI0BAIydAQEAgYCMjIyMjIyMjIzsgQEBAQCAgI0BAIydAQEAgICBAQEBgQEBAOyAgICAgICBAQEBgQEBALAogICAgICAgICAgICAgICAgICAgICAgICdAQEA6QEBAQCArQCBAQEBAQGBAQEAgLEBAQGA6Ojo6LGA6OyNAQEBAYCAgICAgICAgICAgICAgIEBAQCw6Ojo6OmA6OidAQEBAQCAgLEBAQGBAQEAgICAjQEAjJ0BAQCBgOjo6Ojo6Ojo6IC5AQEBAICBAQEAjJ0BAQCAgIEBAQGBAQEA7ICAgICAgIEBAQGBAQEAsCiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQDpAQEBAQCA7LkBAQEBAYEBAQCAsQEBALkBAQEBAIEBAQEBAQGAgICAgICAgICAgICAgICAgQEBALEBAQEBAQCxAQEBAQEAgICAsQEBAYEBAQCAgICNAQCMnQEBAICxAQEBAQEBAQEBAK2BAQEAsICNAQCMnQEBAICAgQEBAYEBAQDsgICAgICAgQEBAYEBAQCwKICAgICAgICAgICAgICAgICAgICAgICAnQEBAOkBAQEBAICAjQEBAQEBgQEBAICxAQEAuQEBAQEArOkBAQEAgICAgICAgICAgICAgICAgICBAQEAsQEBAQEBAIEBAQEBAICAgICxAQEBgQEBAICAgI0BAIydAQEAgLEBAQEBAQEBAQEBAYEBAQEAgQEBAIydAQEAgICBAQEBgQEBAOyAgICAgICBAQEBgQEBALAogICAgICAgICAgICAgICAgICAgICAgICdAQEA6QEBAQEAjYEBAQEBAQGBAQEAgLEBAQC5AQEBAQEAgQEBALiAgICAgICAgICAgICAgICAgIEBAQCxAQEBAQEAjLEBAQCAgICAgLEBAQGBAQEAgICAjQEAjJ0BAQCAsQEBAIyMjIyNAQEBAOkBAQCAjQEAjJ0BAQCAgIEBAQGBAQEA7ICAgICAgIEBAQGBAQEAsCiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQDpAQEBAQEBAQEBAQEBAYEBAQCAsQEBALkBAQCNAQCs6QEBAICAgICAgICAgICAgICAgICAgQEBALEBAQCNAQEBgQEBALCAgICAsQEBAYEBAQDosLEBAQCMnQEBAICxAQDouLi4uLiNAQEAsQEBAICNAQCMnQEBALCw7QEBAYEBAQDsgICAgICAgQEBAYEBAQCwKICAgICAgICAgICAgICAgICAgICAgICAnQEBAOkBAQCNAQEBAQCtAQEBgQEBAICxAQEAuQEBAIEBAQCBAQEBgICAgICAgICAgICAgICAgICBAQEAsQEBAKytAQEAsQEBAICAgICxAQEAgQEBAQEBAQEBAJydAQCMgLEBAQEBAQEBAQEBAOytAQEAgI0BAQCxAQEBAQEBAQEAgQEBAOyAgICAgICBAQEBgQEBALAogICAgICAgICAgICAgICAgICAgICAgICdAQEA6QEBAYEBAQEAjO0BAQGBAQEAgLEBAQC5AQEAgI0BAJztAQEAgICAgICAgICAgICAgICAgIEBAQCxAQEArIEBAQCBAQEBgICAgYEBAQCBAQEBAQEBAQEBgI0BAKyAsQEBAQEBAQEBAQEAgQEBAKyAnQEBAIEBAQEBAQEBAQCBAQEBgICAgICAgIEBAQGBAQEAsCiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQDpAQEAgQEBAQCA7QEBAYEBAQCAsQEBALkBAQCAgQEBAYEBAQC4gICAgICAgICAgICAgICAgQEBALEBAQCsgJ0BAIyxAQEAgICAgQEBAKyAjQEBAQEBALCxAQEA6IC5AQEBAQEBAQEAjIEBAQEAgIC5AQEA6YEBAQEBAQCNgK0BAQCAgICAgICAgQEBAYEBAQCwKICAgICAgICAgICAgICAgICAgICAgICAnQEBAOkBAQCAsQEBAIDtAQEBgQEBAICxAQEBgQEBAICBAQEArJ0BAQCAgYCMjIzsgICAgICAgICBAQEAsQEBAKyAgQEBAYEBAQCwgICAjQEBAIywgICAgIC4nQEBAQCAgICAgICAgICAgIDpAQEBAIyAgIEBAQEArYCAgICAgLiNAQEBAICAgICAgICBAQEBgQEBALAogICAgICAgICAgICAgICAgICAgICAgICdAQEA6QEBAICBAQC4gO0BAQGBAQEAgLEBAQGBAQEAgICBAQEAgQEBAYCBgQEBAJyAgICAgICAgIEBAQCxAQEArICArQEBALEBAQCAgICBAQEBAQEBAQEBAQEBAQEA7ICAuQEBAQEBAQEBAQEBAQEAgICAgLEBAQEBAQEBAQEBAQEBAQGAgICAgICAgIEBAQGBAQEAsCiAgICAgICAgICAgICAgICAgICAgICAgJ0BAQDpAQEAgICdAICA7QEBAYEBAQCAsQEBAYEBAQCAgICtAQCMnQEBAIGBAQEAnICAgICAgICAgQEBALEBAQCsgICBAQEAgQEBALiAgIC5AQEBAQEBAQEBAQEBAKyAgICxAQEBAQEBAQEBAQEBAICAgICAgK0BAQEBAQEBAQEBAQEAsICAgICAgICAgQEBAYEBAQCwKICAgICAgICAgICAgICAgICAgICAgICAnQEAjOkBAQCAgICwgIDtAQEBgQEBAICxAQEBgQEBAICAgIEBAQCBAQEBgYEBAQCcgICAgICAgICBAQEAsQEBAKyAgICdAQCM6QEBAICAgICAnQEBAQEBAQEBAK2AgICAgLkBAQEBAQEBAQEBALCAgICAgICAgICtAQEBAQEBAQEAnICAgICAgICAgICBAQEBgQEBALAo=")
print "." * 200
print "." * 200
print "." * 200
print " " * 90 + base64.b64decode("REVTVFJVQ1RJT04gSU5JVElBVEVEIQ==");
print " " * 93 + base64.b64decode("R29vZGJ5ZSB3b3JsZC4uLg==");
print "." * 200
print "." * 200
print "." * 200
