SlackLogHandler
================

python log handler，用于将日志打到slack


应用场景
---------
运维系统的一些消息时希望通知到开发的。一般是整个发布完成后再抓去处理日志再用邮件等通知开发。
但这样不利于异常处理。希望把发布的一些信息实时的发布出来供开发订阅。


使用说明
--------
.. autoclass:: opsas.utils.SlackLogHandler
   :members: create_session