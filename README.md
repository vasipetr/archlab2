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
Στο αρχείο spec_results έχουν αποθηκευτεί τα αποτελέσματα των παραπάνω εντολών. Ανατρέχοντας στα αρχεία που προέκυψαν (config.ini, config.json, stats.txt) μπορούμε να δούμε τις βασικές παραμέτρους για τον επεξεργαστή που εξομοιώνει ο gem5 όσον αφορά το υποσύστημα
μνήμης.
Πιο συγκεκριμένα:
α)
* sim_insts (ο αριθμός των εντολών που δεσμεύτηκαν από τη CPU)
* Block replacements για την L1 Dcache
* Αριθμός των access στην L2 cache


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
| specbzip  | 0.083962 ||
| specmcf   | 0.064955 ||
| spechmmer | 0.059396 ||
| specsjeng | 0.513528 ||
| speclibm  | 0.174671 ||
