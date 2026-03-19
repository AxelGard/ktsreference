

# retainAll

Retains only the elements in this collection that are contained in the specified collection.

```kotlin
@IgnorableReturnValueinline fun <T> MutableCollection<out T>.retainAll(elements: Collection<T>): Boolean(source)
```

```kotlin
fun main() {
    val numbers = mutableListOf(1, 2, 3, 4, 5)
    val toKeep = listOf(2, 4, 6)

    val wasModified = numbers.retainAll(toKeep)

    println("Modified: $wasModified")
    println("Resulting list: $numbers")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/retain-all.html)

    