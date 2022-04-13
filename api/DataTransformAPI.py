#coding:utf-8
import json
import requests
class DataTransformAPI():
    def __init__(self):
        self.get_url = "http://10.106.0.93:8092/dmp-api/api/AutoModule/DataTransform"

    def DataTransform(self,session,CPDM):
        #准备参数
        data ={
    "Table":[
        {
            "CPMC":"诸暨农商银行“越福盈”2021年第27期封闭净值型理财产品",
            "CPJC":"",
            "GLR":"浙江诸暨农村商业银行股份有限公司",
            "FXJG":"",
            "SFJGH ":"",
            "CPDM":CPDM,
            "DJBM":"td",
            "FXPJ":"",
            "SYLX":"非保本浮动",
            "CPMZ":"",
            "BZ":"",
            "MQFD":"",
            "FXDX":"",
            "FXDXSM":"",
            "FXQD_S":"丰收互联APP、柜面、自助终端等",
            "FXDQ":"",
            "XSQSR":"",
            "XSJZR":"",
            "CPCLR":"2021-12-21",
            "CPDQR":"",
            "ZDCYQX":"",
            "ZDCYQXDW":"",
            "TZQX":"",
            "TZQXDW":"",
            "XSQD":"",
            "XSSM_S":"",
            "DZJE":"",
            "SGSX":"",
            "RGQFXGMSX":"null",
            "CXQFXGMSX":"",
            "FXGMXX":"",
            "SFYXCD":"null",
            "CDGZ":"",
            "CDGZ_2":"",
            "YQSYLSX":"",
            "YQSYLXX":"",
            "YJBJJZSX":"4.05",
            "YJBJJZXX":"4.05",
            "NHTS":"",
            "ZJDZR":"",
            "TGR":"",
            "XSJG":"",
            "YZMS":"",
            "TZXZ":"",
            "SFKZY":"",
            "YHNFTQZZ":"",
            "TQZZTJ":"",
            "SGQRPL_S":"诸暨农商银行“越福盈”2021年第27期封闭净值型理财产品",
            "SGQRSJ":"",
            "SGTJ":"",
            "SHDZSJ_S":"",
            "SHQRPL":"诸暨农商银行“越福盈”2021年第27期封闭净值型理财产品",
            "SHTJ":"",
            "SGHSHSM":"",
            "CPFY":"",
            "CPFY_2":"",
            "SYSM":"业绩比较基准4.05%",
            "TZBDSM":"",
            "QTTZXZ":"",
            "TZCL":"",
            "TZBL":"",
            "GGNR":'诸暨农商银行“越福盈”2021年第27期封闭净值型理财产品理财产品基本信息：理财产品名称诸暨农商银行“越福盈”2021年第27期封闭净值型理财产品理财产品类型非保本浮动收益型理财产品代码SXZJYFY2021027理财产品登记编码C1125221000048投资币种人民币产品发行规模3000万客户类型一般普通客户成立日2021-12-21到期日2022-10-13客户资金到帐日2022-10-13认购期点金额1万业绩比较基准4.05%销售渠道丰收互联APP、柜面、自助终端等发行银行浙江诸暨农村商业银行股份有限公司投资管理人浙江诸暨农村商业银行股份有限公司资金托管银行招商银行股份有限公司杭州分行理财产品风险评级PR2（中低风险）返回列表'
        }
    ],
    "MatchRule":{
        "AliasRow":0,
        "StartRow":0,
        "EndRow":0,
        "StartColumn":0,
        "EndColumn":0,
        "GroupNum":0,
        "ColumnHeader":0,
        "CombineRow":"",
        "CombineColumn":"",
        "SplitTable":"",
        "FilterRows":[

        ],
        "FilterColumns":[

        ],
        "Formulas":[
            {
                "FormulaID":"字符相等替换(All)(GLR,,0,1)",
                "Caption":"管理人",
                "ParaName":"GLR",
                "Formula":"AAEAAAD/////AQAAAAAAAAAMAgAAAExEZWR1Y2UuQ29tbW9uLkZvcm11bGEsIFZlcnNpb249MS4wLjcuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBQEAAAAgRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLkV4cHJlc3Npb24CAAAAFTxOYW1lPmtfX0JhY2tpbmdGaWVsZBs8UGFyYW1ldGVycz5rX19CYWNraW5nRmllbGQBA5UBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tEZWR1Y2UuQ29tbW9uLkZvcm11bGEuUGFyYUJpbmREYXRhLCBEZWR1Y2UuQ29tbW9uLkZvcm11bGEsIFZlcnNpb249MS4wLjcuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsXV0CAAAABgMAAAAX5a2X56ym55u4562J5pu/5o2iKEFsbCkJBAAAAAQEAAAAlQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW0RlZHVjZS5Db21tb24uRm9ybXVsYS5QYXJhQmluZERhdGEsIERlZHVjZS5Db21tb24uRm9ybXVsYSwgVmVyc2lvbj0xLjAuNy4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXQMAAAAGX2l0ZW1zBV9zaXplCF92ZXJzaW9uBAAAJERlZHVjZS5Db21tb24uRm9ybXVsYS5QYXJhQmluZERhdGFbXQIAAAAICAkFAAAAAwAAAAMAAAAHBQAAAAABAAAABAAAAAQiRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLlBhcmFCaW5kRGF0YQIAAAAJBgAAAAkHAAAACQgAAAAKBQYAAAAiRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLlBhcmFCaW5kRGF0YQwAAAAfPEJpbmRpbmdPcHRpb25zPmtfX0JhY2tpbmdGaWVsZBs8Rml4ZWRWYWx1ZT5rX19CYWNraW5nRmllbGQfPEZpeGVkVmFsdWVUZXh0PmtfX0JhY2tpbmdGaWVsZCI8QmluZGluZ0lkZW50aWZpZXI+a19fQmFja2luZ0ZpZWxkHDxGb3JtdWxhTmFtZT5rX19CYWNraW5nRmllbGQcPEZvcm11bGFUZXh0PmtfX0JhY2tpbmdGaWVsZB48TmVzdGVkRm9ybXVsYT5rX19CYWNraW5nRmllbGQnUGFyYURlc2NyaXB0KzxEYXRhVHlwZXM+a19fQmFja2luZ0ZpZWxkJlBhcmFEZXNjcmlwdCs8UGFyYU5hbWU+a19fQmFja2luZ0ZpZWxkKVBhcmFEZXNjcmlwdCs8RGVzY3JpcHRpb24+a19fQmFja2luZ0ZpZWxkJlBhcmFEZXNjcmlwdCs8SXNQYXJhbXM+a19fQmFja2luZ0ZpZWxkElBhcmFEZXNjcmlwdCthbGlhcwQCAQEBAQQDAQEAAShEZWR1Y2UuQ29tbW9uLkZvcm11bGEuUGFyYUJpbmRpbmdPcHRpb25zAgAAACBEZWR1Y2UuQ29tbW9uLkZvcm11bGEuRXhwcmVzc2lvbgIAAAB/U3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQECAAAABff///8oRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLlBhcmFCaW5kaW5nT3B0aW9ucwEAAAAHdmFsdWVfXwAIAgAAAAEAAAAKCgYKAAAAA0dMUgkDAAAACgoJDAAAAAYNAAAADOabv+aNouWvueixoQkNAAAAAAkNAAAADA4AAABOU3lzdGVtLkRhdGEsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5AQcAAAAGAAAAAfH////3////AAAAAAkQAAAACgoJAwAAAAoKCRIAAAAGEwAAAAzmm7/mjaLlhbPns7sJEwAAAAAJEwAAAAEIAAAABgAAAAHs////9////wAAAAAGFQAAAAMwLDEKCgkDAAAACgoJFwAAAAYYAAAADOabv+aNouaWueW8jwkYAAAAAAkYAAAABAwAAAB/U3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQMAAAAGX2l0ZW1zBV9zaXplCF92ZXJzaW9uBgAACAgJGQAAAAIAAAABAAAABRAAAAAVU3lzdGVtLkRhdGEuRGF0YVRhYmxlAwAAABlEYXRhVGFibGUuUmVtb3RpbmdWZXJzaW9uCVhtbFNjaGVtYQtYbWxEaWZmR3JhbQMBAQ5TeXN0ZW0uVmVyc2lvbg4AAAAJGgAAAAYbAAAA5AU8P3htbCB2ZXJzaW9uPSIxLjAiIGVuY29kaW5nPSJ1dGYtMTYiPz4NCjx4czpzY2hlbWEgeG1sbnM9IiIgeG1sbnM6eHM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvWE1MU2NoZW1hIiB4bWxuczptc2RhdGE9InVybjpzY2hlbWFzLW1pY3Jvc29mdC1jb206eG1sLW1zZGF0YSI+DQogIDx4czplbGVtZW50IG5hbWU9IlRhYmxlMSI+DQogICAgPHhzOmNvbXBsZXhUeXBlPg0KICAgICAgPHhzOnNlcXVlbmNlPg0KICAgICAgICA8eHM6ZWxlbWVudCBuYW1lPSLmupDmlbDmja4iIHR5cGU9InhzOnN0cmluZyIgbXNkYXRhOnRhcmdldE5hbWVzcGFjZT0iIiBtaW5PY2N1cnM9IjAiIC8+DQogICAgICAgIDx4czplbGVtZW50IG5hbWU9Iuabv+aNouS4uiIgdHlwZT0ieHM6c3RyaW5nIiBtc2RhdGE6dGFyZ2V0TmFtZXNwYWNlPSIiIG1pbk9jY3Vycz0iMCIgLz4NCiAgICAgIDwveHM6c2VxdWVuY2U+DQogICAgPC94czpjb21wbGV4VHlwZT4NCiAgPC94czplbGVtZW50Pg0KICA8eHM6ZWxlbWVudCBuYW1lPSJ0bXBEYXRhU2V0IiBtc2RhdGE6SXNEYXRhU2V0PSJ0cnVlIiBtc2RhdGE6TWFpbkRhdGFUYWJsZT0iVGFibGUxIiBtc2RhdGE6VXNlQ3VycmVudExvY2FsZT0idHJ1ZSI+DQogICAgPHhzOmNvbXBsZXhUeXBlPg0KICAgICAgPHhzOmNob2ljZSBtaW5PY2N1cnM9IjAiIG1heE9jY3Vycz0idW5ib3VuZGVkIiAvPg0KICAgIDwveHM6Y29tcGxleFR5cGU+DQogIDwveHM6ZWxlbWVudD4NCjwveHM6c2NoZW1hPgYcAAAAiAM8ZGlmZmdyOmRpZmZncmFtIHhtbG5zOm1zZGF0YT0idXJuOnNjaGVtYXMtbWljcm9zb2Z0LWNvbTp4bWwtbXNkYXRhIiB4bWxuczpkaWZmZ3I9InVybjpzY2hlbWFzLW1pY3Jvc29mdC1jb206eG1sLWRpZmZncmFtLXYxIj4NCiAgPHRtcERhdGFTZXQ+DQogICAgPFRhYmxlMSBkaWZmZ3I6aWQ9IlRhYmxlMTEiIG1zZGF0YTpyb3dPcmRlcj0iMCIgZGlmZmdyOmhhc0NoYW5nZXM9Imluc2VydGVkIj4NCiAgICAgIDzmupDmlbDmja4+5rWZ5rGf6K+45pqo5Yac5p2R5ZWG5Lia6ZO26KGM6IKh5Lu95pyJ6ZmQ5YWs5Y+4PC/mupDmlbDmja4+DQogICAgICA85pu/5o2i5Li6PjQxNzgyPC/mm7/mjaLkuLo+DQogICAgPC9UYWJsZTE+DQogIDwvdG1wRGF0YVNldD4NCjwvZGlmZmdyOmRpZmZncmFtPgESAAAADAAAAAkdAAAAAQAAAAEAAAABFwAAAAwAAAAJHgAAAAEAAAABAAAAERkAAAAEAAAABh8AAAAJ5Y2V5YWD5qC8BiAAAAAGc3RyaW5nDQIEGgAAAA5TeXN0ZW0uVmVyc2lvbgQAAAAGX01ham9yBl9NaW5vcgZfQnVpbGQJX1JldmlzaW9uAAAAAAgICAgCAAAAAAAAAP//////////ER0AAAAEAAAABiEAAAAFVGFibGUNAxEeAAAABAAAAAkgAAAADQML",
                "Condition":{
                    "Name":"",
                    "Caption":"",
                    "Content":"",
                    "Parameters":""
                },
                "BeforeQuery":"false"
            },
            {
                "FormulaID":"截取字符串(CPDM,1,4)",
                "Caption":"截取字符",
                "ParaName":"CPDM",
                "Formula":"AAEAAAD/////AQAAAAAAAAAMAgAAAExEZWR1Y2UuQ29tbW9uLkZvcm11bGEsIFZlcnNpb249MS4wLjcuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsBQEAAAAgRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLkV4cHJlc3Npb24CAAAAFTxOYW1lPmtfX0JhY2tpbmdGaWVsZBs8UGFyYW1ldGVycz5rX19CYWNraW5nRmllbGQBA5UBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tEZWR1Y2UuQ29tbW9uLkZvcm11bGEuUGFyYUJpbmREYXRhLCBEZWR1Y2UuQ29tbW9uLkZvcm11bGEsIFZlcnNpb249MS4wLjcuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsXV0CAAAABgMAAAAP5oiq5Y+W5a2X56ym5LiyCQQAAAAEBAAAAJUBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tEZWR1Y2UuQ29tbW9uLkZvcm11bGEuUGFyYUJpbmREYXRhLCBEZWR1Y2UuQ29tbW9uLkZvcm11bGEsIFZlcnNpb249MS4wLjcuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsXV0DAAAABl9pdGVtcwVfc2l6ZQhfdmVyc2lvbgQAACREZWR1Y2UuQ29tbW9uLkZvcm11bGEuUGFyYUJpbmREYXRhW10CAAAACAgJBQAAAAMAAAADAAAABwUAAAAAAQAAAAQAAAAEIkRlZHVjZS5Db21tb24uRm9ybXVsYS5QYXJhQmluZERhdGECAAAACQYAAAAJBwAAAAkIAAAACgUGAAAAIkRlZHVjZS5Db21tb24uRm9ybXVsYS5QYXJhQmluZERhdGEMAAAAHzxCaW5kaW5nT3B0aW9ucz5rX19CYWNraW5nRmllbGQbPEZpeGVkVmFsdWU+a19fQmFja2luZ0ZpZWxkHzxGaXhlZFZhbHVlVGV4dD5rX19CYWNraW5nRmllbGQiPEJpbmRpbmdJZGVudGlmaWVyPmtfX0JhY2tpbmdGaWVsZBw8Rm9ybXVsYU5hbWU+a19fQmFja2luZ0ZpZWxkHDxGb3JtdWxhVGV4dD5rX19CYWNraW5nRmllbGQePE5lc3RlZEZvcm11bGE+a19fQmFja2luZ0ZpZWxkJ1BhcmFEZXNjcmlwdCs8RGF0YVR5cGVzPmtfX0JhY2tpbmdGaWVsZCZQYXJhRGVzY3JpcHQrPFBhcmFOYW1lPmtfX0JhY2tpbmdGaWVsZClQYXJhRGVzY3JpcHQrPERlc2NyaXB0aW9uPmtfX0JhY2tpbmdGaWVsZCZQYXJhRGVzY3JpcHQrPElzUGFyYW1zPmtfX0JhY2tpbmdGaWVsZBJQYXJhRGVzY3JpcHQrYWxpYXMEAgEBAQEEAwEBAAEoRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLlBhcmFCaW5kaW5nT3B0aW9ucwIAAAAgRGVkdWNlLkNvbW1vbi5Gb3JtdWxhLkV4cHJlc3Npb24CAAAAf1N5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0BAgAAAAX3////KERlZHVjZS5Db21tb24uRm9ybXVsYS5QYXJhQmluZGluZ09wdGlvbnMBAAAAB3ZhbHVlX18ACAIAAAABAAAACgoGCgAAAARDUERNCQMAAAAKCgkMAAAABg0AAAAM5oiq5Y+W5a+56LGhCQ0AAAAACQ0AAAABBwAAAAYAAAAB8v////f///8AAAAABg8AAAABMQoKCQMAAAAKCgkRAAAABhIAAAAM5byA5aeL5L2N572uCRIAAAAACRIAAAABCAAAAAYAAAAB7f////f///8AAAAABhQAAAABNAoKCQMAAAAKCgkWAAAABhcAAAAM5oiq5Y+W6ZW/5bqmCRcAAAAACRcAAAAEDAAAAH9TeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1N5c3RlbS5TdHJpbmcsIG1zY29ybGliLCBWZXJzaW9uPTQuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49Yjc3YTVjNTYxOTM0ZTA4OV1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24GAAAICAkYAAAAAQAAAAEAAAABEQAAAAwAAAAJGQAAAAEAAAABAAAAARYAAAAMAAAACRoAAAABAAAAAQAAABEYAAAABAAAAAYbAAAABnN0cmluZw0DERkAAAAEAAAACRsAAAANAxEaAAAABAAAAAkbAAAADQML",
                "Condition":{
                    "Name":"",
                    "Caption":"",
                    "Content":"",
                    "Parameters":""
                },
                "BeforeQuery":"false"
            }
        ],
        "SourceFormulas":[

        ],
        "expand":{
            "Formulas_Origin":{
                "GLR_0":{
                    "dataFormulaFormulaInfo":{
                        "formulaId":"字符相等替换(All)-1_0_0_0_4",
                        "formulaName":"字符相等替换(All)",
                        "form":{
                            "替换对象":"GLR",
                            "替换对象ModalData":{
                                "origin":[
                                    {
                                        "Name":"替换对象",
                                        "type":"Identifier",
                                        "value":"GLR"
                                    }
                                ],
                                "form":{
                                    "Identifier":"GLR"
                                },
                                "tabName":"Identifier"
                            },
                            "替换关系":"replace(浙江诸暨农村商业银行股份有限公司,41782);",
                            "替换关系ModalData":{
                                "tableData":[
                                    {
                                        "_index":0,
                                        "_rowKey":1,
                                        "origin":"浙江诸暨农村商业银行股份有限公司",
                                        "target":"41782"
                                    }
                                ],
                                "origin":[
                                    {
                                        "type":"FixedValue",
                                        "Name":"替换源",
                                        "value":[
                                            "浙江诸暨农村商业银行股份有限公司"
                                        ]
                                    },
                                    {
                                        "type":"FixedValue",
                                        "Name":"替换为",
                                        "value":[
                                            "41782"
                                        ]
                                    }
                                ]
                            },
                            "替换方式":"找不到内容不替换:未勾选;全量匹配:勾选;",
                            "替换方式ModalData":{
                                "form":{

                                },
                                "origin":[
                                    {
                                        "Name":"替换方式",
                                        "type":"FixedValue",
                                        "value":"0,1"
                                    }
                                ]
                            }
                        }
                    }
                },
                "CPDM_1":{
                    "dataFormulaFormulaInfo":{
                        "formulaId":"截取字符串-1_0_0_2_12",
                        "formulaName":"截取字符串",
                        "form":{
                            "截取对象":"CPDM",
                            "截取对象ModalData":{
                                "origin":[
                                    {
                                        "Name":"截取对象",
                                        "type":"Identifier",
                                        "value":"CPDM"
                                    }
                                ],
                                "form":{
                                    "Identifier":"CPDM"
                                },
                                "tabName":"Identifier"
                            },
                            "开始位置":"1",
                            "开始位置ModalData":{
                                "origin":[
                                    {
                                        "Name":"开始位置",
                                        "type":"FixedValue",
                                        "value":"1"
                                    }
                                ],
                                "form":{
                                    "Identifier":"",
                                    "FixedValue":"1"
                                },
                                "tabName":"FixedValue"
                            },
                            "截取长度":"4",
                            "截取长度ModalData":{
                                "origin":[
                                    {
                                        "Name":"截取长度",
                                        "type":"FixedValue",
                                        "value":"4"
                                    }
                                ],
                                "form":{
                                    "FixedValue":"4"
                                },
                                "tabName":"FixedValue"
                            }
                        }
                    }
                }
            }
        }
    },
    "DataMode":0
}
        #发送请求
        response = session.post(self.get_url,json=data)
        #返回响应
        return response

