


(defn merge [a b] 
    (cond
        (empty? a) b
        (empty? b) a
        (> (first a) (first b)) (conj b a)
        :else (conj a b)))


(defn mergesort [l]
    (if (< (length l) 2)
        l
        (merge (mergesort (drop h l) (take h



(defn sort [a] 
    (loop [j 1 k (first a) l a  r []]
        (loop [b (rest l)]
            (if (> k (first b))
                (recur (rest b) 
        )))
