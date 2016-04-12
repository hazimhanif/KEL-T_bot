# KEL-T_bot
A python Telegram robot for KEL-T Monitoring system.
KEL-T is a Log Monitoring System developed by Hazim Hanif. It leverage the power of ELK Stack (Elasticsearch, Logstash and Kibana) for analytics and visualization of logs. The creation of the telegram robot is to enable network analyst and security analyst to monitor the network remotely without being present at the ops center.
Available in mobile phones and laptop, user can query any info regarding the network just by using Telegram Messenger through this KEL-T Bot.

### The monitored logs were:
* McAfee Sidewinder Firewall Log
* Fortigate Firewall Log
* Bind DNS Firewall log

### Prerequisites:
* Elasticseach python connector
* Python 2.7
* Telegram bot API key
* Elasticsearch server
* Telebot python telegram robot wrapper

### How to Use:
1. Install all the prerequisite stuff.
2. Download the robot.
3. Run the robot file (\_init_.py)
3. Open Telegram Messenger in mobile phones or laptop
4. Add the robot to group or interact directly with the robot. e.g @kelt_bot
5. Type in "\start"
6. Type in "\es"
7. Enjoy

Thank you very much for the author of the Telebot python telegram bot wrapper.
