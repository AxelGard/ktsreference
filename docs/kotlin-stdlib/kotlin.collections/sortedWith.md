

# sortedWith

Returns a list of all elements sorted according to the specified comparator.

```kotlin
fun <T> Array<out T>.sortedWith(comparator: Comparator<in T>): List<T>(source)
```

```kotlin
val words = arrayOf("banana", "apple", "cherry")
val sorted = words.sortedWith(Comparator { a, b -> a.length - b.length })
println(sorted)   // [apple, banana, cherry]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sorted-with.html)

    