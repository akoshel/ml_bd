# Homework 1
#### Пункт 1
Скрины: Name_Node_shot.jpg Recourse_manager_shot.jpg

#### Пункт 2
Последовательность команд в P2.txt

#### Пункт 3
Скрипты для среднего - mapper.py, reducer.py
Скрипты для дисперсии - mapper_var.py, reducer_var.py
Итоги расчетов result.txt
Результат выполнения скриптов в папках out_mean, out_var





helpers
```angular2html
mapred streaming -input /AB_NYC_2019.csv -output /out_var -mapper "python mapper_var.py" -reducer "python reducer_var.py" -file /mapper_var.py -file /reducer_var.py
docker cp AB_NYC_2019.csv namenode:/
```