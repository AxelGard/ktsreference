

# groupingBy

Creates a Grouping source from a char sequence to be used later with one of group-and-fold operations using the specified keySelector function to extract a key from each character.

```kotlin
inline fun <K> CharSequence.groupingBy(crossinline keySelector: (Char) -> K): Grouping<Char, K>(source)
```

```kotlin
val text = "hello world"

val charCounts = text.groupingBy { it }.eachCount()
println(charCounts)   // {h=1, e=1, l=3, o=2,  =1, w=1, r=1, d=1}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/grouping-by.html)

    