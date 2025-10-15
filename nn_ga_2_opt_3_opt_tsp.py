import matplotlib.pyplot as plt
import random
from math import pi, sin, cos, asin

coc = {
    'Adana': (35.3213, 37.0025),'Adıyaman': (38.2765, 37.7648),
    'Afyonkarahisar': (30.5399, 38.7637),'Ağrı': (43.0503, 39.7191),
    'Aksaray': (34.0295, 38.3687),'Amasya': (35.8353, 40.6539),
    'Ankara': (32.8597, 39.9334),'Antalya': (30.7133, 36.8969),
    'Ardahan': (42.7022, 41.1105),'Artvin': (41.8190, 41.1828),
    'Aydın': (27.8440, 37.8483),'Balıkesir': (27.8896, 39.6484),
    'Bartın': (32.3377, 41.6358),'Batman': (41.1214, 37.8812),
    'Bayburt': (40.2280, 40.2604),'Bilecik': (30.0561, 40.1501),
    'Bingöl': (40.4963, 38.8847),'Bitlis': (42.1082, 38.3938),
    'Bolu': (31.5788, 40.7351),'Burdur': (30.2833, 37.7207),
    'Bursa': (29.0610, 40.1826),'Çanakkale': (26.4064, 40.1553),
    'Çankırı': (33.6167, 40.5983),'Çorum': (34.9516, 40.5489),
    'Denizli': (29.0875, 37.7838),'Diyarbakır': (40.2370, 37.9188),
    'Düzce': (31.1636, 40.8438),'Edirne': (26.5700, 41.6772),
    'Elazığ': (39.2232, 38.6853),'Erzincan': (39.5042, 39.7507),
    'Erzurum': (41.2769, 39.9057),'Eskişehir': (30.5256, 39.7667),
    'Gaziantep': (37.3833, 37.0662),'Giresun': (38.3874, 40.9175),
    'Gümüşhane': (39.4788, 40.4600),'Hakkari': (43.7370, 37.5735),
    'Hatay': (36.4018, 36.2025),'Iğdır': (44.0398, 39.9226),
    'Isparta': (30.5537, 37.7648),'İstanbul': (28.9784, 41.0082),
    'İzmir': (27.1287, 38.4192),'Kahramanmaraş': (36.9371, 37.5738),
    'Karabük': (32.6270, 41.2047),'Karaman': (33.2150, 37.1818),
    'Kars': (43.0946, 40.6013),'Kastamonu': (33.7753, 41.3887),
    'Kayseri': (35.4934, 38.7225),'Kilis': (37.1154, 36.7184),
    'Kırıkkale': (33.5017, 39.8469),'Kırklareli': (27.2167, 41.7333),
    'Kırşehir': (34.1636, 39.1458),'Kocaeli': (29.9204, 40.8533),
    'Konya': (32.4846, 37.8746),'Kütahya': (29.6115, 39.4242),
    'Malatya': (38.3116, 38.3552),'Manisa': (27.4221, 38.6191),
    'Mardin': (40.7323, 37.3125),'Mersin': (34.6395, 36.8121),
    'Muğla': (28.3557, 37.2153),'Muş': (41.4918, 38.9462),
    'Nevşehir': (34.7127, 38.6241),'Niğde': (34.6794, 37.9667),
    'Ordu': (37.8733, 40.9790),'Osmaniye': (36.2476, 37.0681),
    'Rize': (40.5110, 41.0201),'Sakarya': (30.4075, 40.7737),
    'Samsun': (36.3437, 41.2867),'Siirt': (41.9333, 37.9333),
    'Sinop': (35.1532, 42.0231),'Sivas': (37.0166, 39.7477),
    'Şanlıurfa': (38.7939, 37.1670),'Şırnak': (42.4559, 37.5166),
    'Tekirdağ': (27.5149, 40.9780),'Tokat': (36.5546, 40.3167),
    'Trabzon': (39.7168, 41.0015),'Tunceli': (39.5506, 39.1060),
    'Uşak': (29.4058, 38.6743),'Van': (43.3718, 38.5012),
    'Yalova': (29.2769, 40.6556),'Yozgat': (34.8070, 39.8194),
    'Zonguldak': (31.7936, 41.4564)
}

class City:
    def __init__(self, n, c):
        self.name = n
        self.coordinate = c

cities = [City(p, coc[p]) for p in coc]

for i in range(len(cities)):
    cities[i].idx=i

def find_distance(A, B, r=6371.0088):
    t1 = pi * ((90 - A[1]) / 180); a1 = pi * (A[0] / 180)
    t2 = pi * ((90 - B[1]) / 180); a2 = pi * (B[0] / 180)
    x1 = r * sin(t1) * cos(a1); y1 = r * sin(t1) * sin(a1); z1 = r * cos(t1)
    x2 = r * sin(t2) * cos(a2); y2 = r * sin(t2) * sin(a2); z2 = r * cos(t2)
    d = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)**0.5
    beta = asin(d/(2*r))
    return 2 * beta * r

N = len(cities)
dist = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        d = find_distance(cities[i].coordinate, cities[j].coordinate)
        dist[i][j] = dist[j][i] = d

def total_distance_cycle(path):
    s = 0
    n = len(path)
    for i in range(n):
        s += dist[path[i].idx][path[(i+1) % n].idx]
    return s

def journey(start_city):
    start = next(c for c in cities if c.name == start_city)
    unvisited = [c for c in cities if c is not start]
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda c: find_distance(cur.coordinate, c.coordinate))
        path.append(nxt) 
        unvisited.remove(nxt)
        cur = nxt
    return path  

def nn_cycle_best():
    best_len =float('inf')
    for s in coc.keys():
        p = journey(s)
        L = total_distance_cycle(p)
        if L < best_len:
            best_path, best_len = p, L
    return best_path

def parent_select(pop, k, fitness_fn):
    cand = random.sample(pop, k)
    cand.sort(key=fitness_fn)
    return cand[0]

def ordered_crossover(p1, p2):
    n = len(p1)
    i, j = sorted(random.sample(range(n), 2))
    child = [None]*n
    child[i:j] = p1[i:j]
    it = (g for g in p2 if g not in child)
    for t in range(n):
        if child[t] is None:
            child[t] = next(it)
    return child

def mutate_swap(perm, rate):
    if random.random() < rate:
        i, j = random.sample(range(len(perm)), 2)
        perm[i], perm[j] = perm[j], perm[i]

def mutate_two_opt(perm, rate):
    if random.random() < rate:
        i, j = sorted(random.sample(range(len(perm)), 2))
        if j - i > 1:
            perm[i:j] = reversed(perm[i:j])

def genetic_tsp_cycle(pop_size, generation, elit_rate, k, mut_two_opt_rate, mutation_rate, seed=None):
    population = []
    if seed != None:
        population.append(seed)
    while len(population) < pop_size:
        p = cities[:]
        random.shuffle(p)
        population.append(p)
    elite_count = max(1, int(pop_size * elit_rate))
    best_perm, best_distance = None, float('inf')
    for _ in range(generation):
        population.sort(key=total_distance_cycle)
        d0 = total_distance_cycle(population[0])
        if d0 < best_distance:  
            best_distance = d0
            best_perm = population[0][:]
        elites = population[:elite_count]
        while len(elites) < pop_size:
            p1 = parent_select(population, k, total_distance_cycle)
            p2 = parent_select(population, k, total_distance_cycle)
            child = ordered_crossover(p1, p2)
            mutate_swap(child, mutation_rate)
            mutate_two_opt(child, mut_two_opt_rate)
            elites.append(child)
        population = elites
    return best_perm

def two_opt(path):
    n = len(path)
    best = path[:]
    improved = True
    while improved:
        improved = False
        for i in range(n - 1):
            a, b = best[i], best[(i + 1) % n]
            for j in range(i + 2, n):                           
                c, d = best[j], best[(j + 1) % n]
                old = dist[a.idx][b.idx] + dist[c.idx][d.idx]
                new = dist[a.idx][c.idx] + dist[b.idx][d.idx]    
                if new < old:
                    best[i + 1 : j + 1] = reversed(best[i + 1 : j + 1])
                    improved = True
    return best

def three_opt(path):
    n=len(path)
    best=path[:]
    best_dist=total_distance_cycle(best)

    def candidates(path,i,j,k):
        A=path[:i]; B=path[i:j]; C=path[j:k]; D=path[k:]

        paths=[A+B[::-1]+C+D,
               A+B+C[::-1]+D,
               A+B[::-1]+C[::-1]+D,
               A + C + B + D,
               A+C[::-1]+B+D,
               A+C+B[::-1]+D,
               A+C[::-1]+B[::-1]+D]
        return paths
    
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    for cand in candidates(best, i, j, k):
                        L = total_distance_cycle(cand)
                        if L < best_dist:
                            best = cand
                            best_dist = L
                            improved = True
    return best

def plot_cycle(path, title):
    xs = [c.coordinate[0] for c in path] + [path[0].coordinate[0]]
    ys = [c.coordinate[1] for c in path] + [path[0].coordinate[1]]
    plt.figure(figsize=(20,10))
    plt.plot(xs, ys, '--o')
    for c in path:
        x, y = c.coordinate
        plt.text(x+0.05, y+0.05, c.name, fontsize=9)
    plt.title(title) 
    plt.show()


nn_path = nn_cycle_best()

plot_cycle(nn_path,f'NN Cycle: {total_distance_cycle(nn_path):.1f} km')

nn_path_2opt=two_opt(nn_path)
plot_cycle(nn_path_2opt,f'NN+2opt Cycle: {total_distance_cycle(nn_path_2opt):.1f} km')

nn_path_2_3opt=three_opt(nn_path_2opt)
plot_cycle(nn_path_2_3opt,f'NN+2+3opt Cycle: {total_distance_cycle(nn_path_2_3opt):.1f} km')



ga_path = genetic_tsp_cycle(pop_size=300,                                   
                            generation=1000,
                            elit_rate=0.10,
                            k=10,
                            mut_two_opt_rate=0.15,
                            mutation_rate=0.15,
                            seed=nn_path_2_3opt)

plot_cycle(ga_path,f'NN+2opt+3opt+GA Cycle: {total_distance_cycle(ga_path):.1f} km')


