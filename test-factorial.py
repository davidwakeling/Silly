import requests
import unittest
from factorial import app

mock = app.test_client()

class Testing(unittest.TestCase):
  ###########################################################
  ## Test [1]                                              ##
  ###########################################################
  def test1(self):
    argument = 6
    result   = 720

    hdrs = {"Content-Type":"application/json"}
    js   = {"argument":argument}
    rsp  = mock.post("/factorial",headers=hdrs,json=js)

    self.assertEqual(rsp.status_code,200)
    self.assertEqual(result,rsp.json["result"])
