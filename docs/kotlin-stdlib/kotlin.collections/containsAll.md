

# containsAll

Checks if all elements in the specified collection are contained in this collection.

```kotlin
inline fun <T> Collection<T>.containsAll(elements: Collection<T>): Boolean(source)
```

```kotlin
val mainList = listOf("apple", "banana", "cherry", "date")
val subList = listOf("banana", "cherry")

println(mainList.containsAll(subList))   // Prints: true

val missingList = listOf("banana", "fig")
println(mainList.containsAll(missingList)) // Prints: false
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/contains-all.html)

    