Пункт 1
Скрины: Name_Node_shot.jpg Recourse_manager_shot.jpg

Пункт 2
P2.txt

Пункт 3
result.txt

helpers
```angular2html
mapred streaming -input /AB_NYC_2019.csv -output /out_var -mapper "python mapper_var.py" -reducer "python reducer_var.py" -file /mapper_var.py -file /reducer_var.py
docker cp AB_NYC_2019.csv namenode:/
```