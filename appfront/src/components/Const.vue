<script>
const CONSTGET = {
  SUCCESS: 'success',
  FAILED: 'failed',
  WRONG_PASSWORD: 'wrong password',
  FAIL_MODIFY: 'fail to midify',
  EMAIL_REGISTERED: 'this email has been registered',
  FAIL_SIGN_UP: 'fail to sign up',
  ACCOUNT_NOT_ACTIVETED: 'account not be activated',
  ACCOUNT_LOGGED_OFF: 'account has been logged off',
  ACCOUNT_LOGGED_IN: 'account has been logged in',
  WRONG_ACCOUNT: 'wrong account',
  INVALID: 'invalid',
  EXPIRED: 'expired',
  MAILBOX_REGISTERED: 'the mailbox has been registered',
//   INVITE_FAILURE: 'invite failure',
  ERROR: 'error',
//   CUSTOMER_NOT_EXIST: 'not exist this customer',
  FAIL_LOG_OFF: 'fail to log off',
  FAIL_INQUIRE_INFORMATION: 'fail to inquire information',
//   DIALOGID_NOT_EXIST: 'not exist this dialogID',
//   SID_NOT_EXIST: 'not exist this SID',
//   RID_NOT_EXIST: 'not exist this RID',
//   EID_NOT_EXIST: 'eid not in request.session',
//   CID_NOT_EXIST: 'cid not in request.session',
//   ACCOUNT_ACTIVITED: 'account has been activated'
}
const CONSTSHOW = {
  WRONG_PASSWORD: '密码错误',
  FAIL_MODIFY: '修改失败',
  EMAIL_REGISTERED: '该邮箱已被注册',
  FAIL_SIGN_UP: '注册失败',
  ACCOUNT_NOT_ACTIVETED: '账号未激活',
  ACCOUNT_LOGGED_OFF: '账号已被注销',
  WRONG_ACCOUNT: '账号错误',
  INVALID: '激活码无效',
  EXPIRED: '激活码已过期',
  MAILBOX_REGISTERED: '该邮箱已被注册',
  INVITE_FAILURE: '邀请失败',
  ERROR: '发生错误',
  CUSTOMER_NOT_EXIST: '客服不存在',
  FAIL_LOG_OFF: '账号注销失败',
  FAIL_INQUIRE_INFORMATION: '信息获取失败',
  DIALOGID_NOT_EXIST: '会话不存在',
  SID_NOT_EXIST: 'SID不存在',
  RID_NOT_EXIST: 'RID不存在',
  EID_NOT_EXIST: '登录失败',
  CID_NOT_EXIST: '登录失败',
  ACCOUNT_ACTIVITED: '账号已经激活过了'
}

export default {
  CONSTGET,
  CONSTSHOW
}
</script>