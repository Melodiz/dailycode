### Задача

Кеша получил задачу на стажировке в IT компании: с помощью машинного обучения повысить счастье новых пользователей сервиса. Для этого он должен использовать древний сервис, который может измерять счастье, но только для фиксированного множества пользователей. Кеша должен сделать предсказания для пользователей и получить от сервиса значение производной неизвестной функции потерь для каждого предсказания. Цель - максимально приблизить предсказания к неизвестным таргетам в смысле функции потерь.

### Формат ввода

1. Первая строка содержит три целых числа:
   - `N` (500 <= N <= 1000): количество объектов в выборке.
   - `k` (10 <= k <= 20): число признаков.
   - `m` (10 <= m <= 100): количество итераций.

2. Следующие `N` строк содержат `k` чисел, описывающих признаки каждого объекта.

### Формат вывода

1. Выведите `m` строк, каждая из которых содержит `N` чисел - прогнозы модели для каждого объекта.
2. После каждой из первых `m-1` строк, выведите строку с `N` числами - значениями производной функции потерь для каждого объекта.
3. После последней строки предсказаний, обратная связь не предоставляется.

### Указания

- В конце каждой строки с предсказаниями необходимо сделать перевод строки и сбросить буфер вывода.
- Используйте соответствующие функции для сброса буфера вывода в вашем языке программирования.

### Примечания

Задача напоминает алгоритм градиентного бустинга, где итоговая модель является композицией базовых моделей, каждая из которых приближает антиградиент функционала ошибки.