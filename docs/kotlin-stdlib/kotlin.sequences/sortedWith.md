

# sortedWith

Returns a sequence that yields elements of this sequence sorted according to the specified comparator.

```kotlin
fun <T> Sequence<T>.sortedWith(comparator: Comparator<in T>): Sequence<T>(source)
```

```kotlin
val fruits = sequenceOf("pear", "apple", "banana", "kiwi")

val sortedByLength = fruits.sortedWith(Comparator { a, b -> a.length - b.length })

sortedByLength.forEach(::println)
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/sorted-with.html)

    