

# toSortedSet

Returns a new SortedSet of all characters.

```kotlin
fun CharSequence.toSortedSet(): SortedSet<Char>(source)
```

```kotlin
fun main() {
    val text = "kotlin"
    val sortedSet: SortedSet<Char> = text.toSortedSet()
    println(sortedSet)  // Output: [i, k, l, n, o, t]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/to-sorted-set.html)

    