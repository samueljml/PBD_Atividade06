from matplotlib import pyplot as plt

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

nomes = ( item['name'] for item in users )

friendships = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    return len(user["friends"])

all_number_of_friends = [number_of_friends(users[i]) for i,j in enumerate(users)]
usuarios = [users[i]["name"] for i,j in enumerate(users)]

#================================================================================
#exercicio numero 1

plt.plot(usuarios, all_number_of_friends, color="blue", marker='o', linestyle="solid")
plt.title('Número de amigos por usuário')
plt.ylabel('Número de amigos')
plt.xlabel('Usuários')
plt.yticks([i+1 for i in range(3)])
plt.show()
#=================================================================================

interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodel"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"),(5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (8, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data"),
]

qts_words_interests = {}

for _, interest in interests:
    interest = interest.split()
    for word in interest:
        if word in qts_words_interests:
            qts_words_interests[word] += 1
        else:
            qts_words_interests[word] = 1 

plt.bar(
    qts_words_interests.keys(),
    qts_words_interests.values(),
    0.7
)

#================================================================================
#Exercicio 4

plt.title ("Palavras em interesse")
plt.xlabel ("Palavras")
plt.ylabel ("Frequencia")
plt.yticks([i+1 for i in range(3)])
plt.tick_params(axis='x', rotation=70)
plt.show()
#================================================================================

salaries_and_tenures  = [
    (83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5),
    (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)
]

salaries = []
tenures = []

for salary, tenure in salaries_and_tenures:
    salaries.append(salary)
    tenures.append(tenure)

labels = ([user["name"] for user in users])

for label, tenure, salary in zip(labels, tenures, salaries):
    plt.annotate(
        label,
        xy = (tenure, salary), # o ponto
        xytext = (5, -5), #o quão longe está o texto do ponto
        textcoords = 'offset points'
    )

#=======================================================================
#Exercicio 2
plt.scatter (tenures, salaries)
plt.title ("Tempo de experiência vs. Salário")
plt.xlabel ("Tempo de experiência (anos)")
plt.ylabel ("Salário")
plt.xticks([i for i in range(11)])
plt.show()
#=======================================================================

tenure_and_account_type = [
 (0.7, 'paid'),
 (1.9,'unpaid'),
 (2.5,'paid'),
 (4.2,'unpaid'),
 (6,'unpaid'),
 (6.5,'unpaid'),
 (7.5,'unpaid'),
 (8.1,'unpaid'),
 (8.7,'paid'),
 (10,'paid')
]

paidtxt = ['paid','paid','paid','paid']
unpaidtxt = ['unpaid','unpaid','unpaid','unpaid','unpaid','unpaid']


media_pagantes = 0
qtdPaid = 0
media_nao_pagantes = 0
qtdUnpaid = 0
    
for tenure, account in tenure_and_account_type:
    if account == 'paid':
        media_pagantes += tenure
        qtdPaid += 1
    else:
        media_nao_pagantes += tenure 
        qtdUnpaid += 1

media_pagantes /= qtdPaid
media_nao_pagantes /= qtdUnpaid

#=======================================================================
#Exercicio 3
plt.bar (
   ['paid'],
   media_pagantes,
   0.5 # largura de 8 para cada barra
)
plt.bar (
    ['unpaid'],
   media_nao_pagantes,
   0.5 # largura de 8 para cada barra
)
plt.axis ([-0.5, 1.5, 0, 6])

plt.ylabel("Tempo de experiência (anos)")
plt.title ("Média de salários de pagantes e não pagantes")
plt.show()

