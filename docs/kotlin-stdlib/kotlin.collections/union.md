

# union

Returns a set containing all distinct elements from both collections.

```kotlin
infix fun <T> Array<out T>.union(other: Iterable<T>): Set<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3)
    val moreNumbers = listOf(3, 4, 5)

    val unionSet: Set<Int> = numbers union moreNumbers

    println(unionSet) // Output: [1, 2, 3, 4, 5]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/union.html)

    