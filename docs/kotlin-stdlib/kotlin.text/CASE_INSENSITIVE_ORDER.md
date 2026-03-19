

# CASE_INSENSITIVE_ORDER

A Comparator that orders strings ignoring character case.

```kotlin
expect val String.Companion.CASE_INSENSITIVE_ORDER: Comparator<String>(source)
```

```kotlin
import kotlin.text.String.Companion.CASE_INSENSITIVE_ORDER

fun main() {
    val names = listOf("banana", "Apple", "cherry", "apple", "Banana")
    
    val sorted = names.sortedWith(CASE_INSENSITIVE_ORDER)
    println(sorted) // [Apple, apple, banana, Banana, cherry]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/-c-a-s-e_-i-n-s-e-n-s-i-t-i-v-e_-o-r-d-e-r.html)

    