

# sortedSetOf

Returns a new java.util.SortedSet with the given elements.

```kotlin
fun <T> sortedSetOf(vararg elements: T): TreeSet<T>(source)
```

```kotlin
val numbers = sortedSetOf(5, 3, 8, 1, 4)

for (n in numbers) {
    println(n)   // prints: 1 3 4 5 8
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-set-of.html)

    