# Αρχιτεκτονική Προηγμένων Υπολογιστών - Εργαστήριο 2
## Εργαστήριο Β - Ομάδα 6

### Βήμα 1
Διαδοχική εκτέλεση των benchmarks χρησιμοποιώντας τις παρακάτω εντολές:
```
 ./build/ARM/gem5.opt -d spec_results/specbzip configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/401.bzip2/src/specbzip -o "spec_cpu2006/401.bzip2/data/input.program 10" -I 100000000
```
```
./build/ARM/gem5.opt -d spec_results/specmcf configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/429.mcf/src/specmcf -o "spec_cpu2006/429.mcf/data/inp.in" -I 100000000
```
```
./build/ARM/gem5.opt -d spec_results/spechmmer configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/456.hmmer/src/spechmmer -o "--fixed 0 --mean 325 --num 45000 --sd 200 --seed 0
spec_cpu2006/456.hmmer/data/bombesin.hmm" -I 100000000
```
```
./build/ARM/gem5.opt -d spec_results/specsjeng configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/458.sjeng/src/specsjeng -o
"spec_cpu2006/458.sjeng/data/test.txt" -I 100000000
```
```
./build/ARM/gem5.opt -d spec_results/speclibm configs/example/se.py --cpu-type=MinorCPU --caches --l2cache -c spec_cpu2006/470.lbm/src/speclibm -o "20 spec_cpu2006/470.lbm/data/lbm.in 0 1 spec_cpu2006/470.lbm/data/100_100_130_cf_a.of" -I 100000000
```
1)
Στο αρχείο spec_results έχουν αποθηκευτεί τα αποτελέσματα των παραπάνω εντολών. Ανατρέχοντας στα αρχεία που προέκυψαν (config.ini, config.json, stats.txt) μπορούμε να δούμε τις βασικές παραμέτρους για τον επεξεργαστή που εξομοιώνει ο gem5 όσον αφορά το υποσύστημα μνήμης.
Πιο συγκεκριμένα:
α)
* system.cpu.committedInsts = ο αριθμός των εντολών που δεσμεύτηκαν από τη CPU
* system.cpu.dcache.replacements = ο αριθμός των block replacements για την L1 Dcache
* system.l2.overall_accesses::total = ο αριθμός των access στην L2 cache

|Benchmark|Committed Instructions|L1 Dcache Block Replacements| L2 cache Accesses|
|:-------:|:--------------------:|:--------------------------:|:----------------:|
|specbzip |100.000.001           |710.569                     |712.341           |
|specmcf  |100.000.001           |54.452                      |724.390           |
|spechmmer|100.000.000           |65.718                      |70.563            |
|specsjeng|100.000.000           |5.262.377                   |5.264.051         |
|speclibm |100.000.000           |1.486.955                   |1.488.538         |


2)
Ανοίγοντας το αρχείο stats.txt για κάθε ένα από τα benchmarks βλέπουμε τα εξής:
* sim_seconds = Χρόνος εκτέλεσης
* system.cpu.cpi = CPI (Cycles per Instruction)
* dcache.overall_miss_rate::total = Miss Rate για την L1 Data cache
* icache.overall_miss_rate::total = Miss Rate για την L1 Instruction cache
* l2.overall_miss_rate::total = Miss Rate για την L2 cache

| Benchmark | Χρόνος Εκτέλεσης (s) | CPI       | L1 Data cache MR | L1 Instruction cache MR | L2 cache MR |
| :-------: | :------------------: | :-------: | :--------------: | :---------------------: | :---------: |
| specbzip  | 0.083982             | 1.679650  | 0.014798         | 0.000077                | 0.282163    |
| specmcf   | 0.064955             | 1.299095  | 0.002108         | 0.023612                | 0.055046    |
| spechmmer | 0.059396             | 1.187917  | 0.001637         | 0.000221                | 0.077760    |
| specsjeng | 0.513528             | 10.270554 | 0.121831         | 0.000020                | 0.999972    |
| speclibm  | 0.174671             | 3.493415  | 0.060972         | 0.000094                | 0.999944    |

* Διάγραμμα για Χρόνο Εκτέλεσης


![Figure_1](https://user-images.githubusercontent.com/73646657/145490473-015f51f4-e5ff-4fe7-a023-615df8335582.png)

* Διάγραμμα για CPI


![Figure_2](https://user-images.githubusercontent.com/73646657/145490488-c27cca5f-65dd-4a5e-90da-1d09a6f5cc22.png)

* Διάγραμμα για L1 Dcache Miss Rate


![Figure_3](https://user-images.githubusercontent.com/73646657/145490493-a65b66ed-d31e-4159-b73e-3549183bf08a.png)
κριν
* Διάγραμμα για L1 Icache Miss Rate


![Figure_4](https://user-images.githubusercontent.com/73646657/145490502-5819cf5e-eba3-4fa2-bd4d-1ef64048c9cc.png)

* Διάγραμμα για L2 cache

![Figure_5](https://user-images.githubusercontent.com/73646657/145490515-5ee8fd77-a2e0-45ed-bd7f-1fd49d07df9e.png)

Από τα διαγράμματα φαίνεται ότι ο χρόνος εκτέλεσης, το CPI, το L1 Dcache και το L2 cache έχουν ανάλογες διαβαθμίσεις, ενώ το L1 Instruction cache είναι ανεξάρτητο. Το benchmark specsjeng έχει τον πιο αργό χρόνο εκτέλεσης και CPI που ξεπερνάει κατά πολύ τη μονάδα, ενώ το specmcf έχει το μεγαλύτερο miss rate στην L1 Icache. Τέλος, τα benchmarks specsjeng και speclibm φαίνεται να έχουν σχεδόν 100% ρυθμό αστοχίας, όταν κάνουν access στην L2 cache.

3)
Όπως διαπιστώθηκε και στο προηγούμενο εργαστήριο το default cpu-clock είναι 2GHz. Με το flag -cpu--clock=1.5GHz εκτελούμε ξανά τα benchmarks και ελέγχουμε στα δύο αρχεία stats.txt, που έχουν προκύψει για κάθε benchmark, τις παραμέτρους system.clk_domain.clock και system.cpu_clk_domain.clock. Και στις δύο συχνότητες, η παράμετρος system.clk_domain.clock παραμένει ίδια και ίση με 1000 (Clock period in ticks), ενώ η παράμετρος system.cpu_clk_domain.clock είναι διαφορετική. Στην πρώτη προσομοίωση, που δε χρησιμοποιήθηκε σημαία για τον ορισμό του cpu-clock, βλέπουμε ότι η περίοδος είναι ίση με 500ps και στη δεύτερη είναι 667ps. Συμπεραίνουμε, λοιπόν, ότι η πρώτη παράμετρος αναφέρεται στο ρολόι του συστήματος, το οποίο έχει συχνότητα σταθερή και ίση με 1GHz. Η δεύτερη παράμετρος αναφέρεται στο ρολόι της CPU και γι'αυτό, κατά την πρώτη προσομοίωση που δε χρησιμοποιούμε σημαία, η συχνότητα του είναι ίση με 2GHz (T=500ps), δηλ. ίση με την default, ενώ στη δεύτερη προσομοίωση είναι ίση με 1.5GHz (667ps) όπως ακριβώς θέσαμε.
Στο ίδιο συμπέρασμα καταλήγουμε και ελέγχωντας το αρχείο config.json στο σύστημα με 1.5GHz.

| Benchmark | 2GHz     | 1.5GHz |
|:---------:|:--------:|:------:|
| specbzip  | 0.083962 |0.109754|
| specmcf   | 0.064955 |0.086162|
| spechmmer | 0.059396 |0.079149|
| specsjeng | 0.513528 |0.581937|
| speclibm  | 0.174671 |0.205034|

Καθώς μειώνεται η συχνότητα, αυξάνεται ανάλογα και ο χρόνος εκτέλεσης, εκτός από την περίπτωση των benchmarks specsjeng και speclibm στα οποία δεν αυξήθηκε εξίσου σημαντικά. Συνεπώς, δεν μπορούμε να πούμε ότι έχουμε τέλειο scaling. Αυτό μπορεί να οφείλεται επειδή τα συγκεκριμένα προγράμματα έχουν με διαφορά μεγαλύτερο ρυθμό αστοχίας σε L1 Dcache και L2 cache σε σχέση με τα υπόλοιπα, πράγμα που είναι λογικό να προκαλεί καθυστερήσεις αφού ο επεξεργαστής πρέπει να κάνει access αλλού για να βρει την πληροφορία που ψάχνει.
Αν προσθέσουμε επεξεργαστή?????

### Βήμα 2
Μέσα από το αρχείο config.ini βλέπουμε τις default τιμές των παραμέτρων που ζητούμαστε να ελέγξουμε και να αλλάξουμε για τη μέγιστη επίδοση:
* L1 Dcache, L1 Icache, L2 cache Associativity: 2, 2, 8 αντίστοιχα
* Block size: 64
* Μέγεθος Cache Line: 64
* L1 Dcache, L1 Icache, L2 cache Size Allocation: 65536, 32768, 2.097.152 αντίστοιχα

### Βήμα 3
Από την βιβλιογραφία γνωρίζουμε ότι όσο μεγαλώνει μια μνήμη τόσο αυξάνει και το κόστος της. Στόχος μας είναι να ορίσουμε κάποιες βαρύτητες για τους παράγοντες που χρησιμοποιήσαμε στο δεύτερο βήμα, έτσι ώστε να έχουμε όσο το δυνατόν μικρότερο κόστος και βέλτιστο CPI. Όπως έχει γίνει εμφανές από το δεύτερο βήμα, ο κάθε παράγοντας επηρεάζει το CPI σε διαφορετικό βαθμό. Παρακάτω βλέπουμε πως , αντίστοιχα, αυτοί οι παράγοντες επηρεάζουν το κόστος με βάση τα συμπεράσματα από την μελέτη μας.
Η συνάρτηση του κόστους μας θα έχει μια τέτοια μορφή:
```
Cost = a(L1isize + L1dsize) + β(L1iassoc + L1dassoc) + γ(L2size) + δ(L2assoc) + ε(cache line size)
```
*	**Βαρύτητα α:** Το μέγεθος την μνήμης cache L1 είναι αυτό με το μεγαλύτερο κόστος σε σχέση με τα άλλα στοιχεία.
*	**Βαρύτητα β:** Αύξηση του associativity αυξάνει την πολυπλοκότητα και αντίστοιχα το κόστος. Συγκεκριμένα για το associativity της L1, η βαρύτητα του στην συνάρτηση κόστους μας θα είναι μεγάλη, σχεδόν αντίστοιχη της βαρύτητας α.
*	**Βαρύτητα γ και βαρύτητα δ:** Το μέγεθος της μνήμης L2 αν και σημαντικό για την λειτουργία της CPU μας είναι αρκετά μικρότερο από αυτό της L1. Θα ισχύει το αντίστοιχο για το associativity της.
*	**Βαρύτητα ε:** Το μέγεθος της cache line size επηρεάζει το κόστος λιγότερο από όλα τα υπόλοιπα στοιχεία και για αυτά θα έχει ην αντίστοιχη βαρύτητα.
Μετά από τα παραπάνω, η συνάρτησή μας παίρνει την εξής μορφή:
```
Cost = 0.4(L1isize + L1dsize) + 0.3(L1iassoc + L1dassoc) + 0.15(L2size) + 0.1(L2assoc) + 0.05(cache line size)
```
