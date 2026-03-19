

# flatMapIndexed

Returns a single list of all elements yielded from results of transform function being invoked on each element and its index in the original array.

```kotlin
@JvmName(name = "flatMapIndexedIterable")inline fun <T, R> Array<out T>.flatMapIndexed(transform: (index: Int, T) -> Iterable<R>): List<R>(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3)

val result = numbers.flatMapIndexed { index, value ->
    List(index + 1) { "$value-$index" }   // create a list of strings
}

println(result)   // prints: [1-0, 2-1, 2-1, 3-2, 3-2, 3-2]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/flat-map-indexed.html)

    