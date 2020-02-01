config client
=============


应用场景
--------
在接手运维一些遗留项目时，发现一个配置地狱。项目时间长或者经手人多了之后。

由于：

 - 可能会同时从环境变量，配置文件，配置中心客户端等同时获取配置
 - 然后配置之间有优先级覆盖关系

导致在多个环境或者线上trouble shooting时，实际生效的配置项及配置项来源不够可视化。
因此借照springboot application.yaml的形式。将一个项目使用到的所有配置放在jinja2渲染的yaml文件中。
这样部署维护就非常清晰了



使用说明
--------
.. autoclass:: opsas.utils.ConfigClient
   :members:


