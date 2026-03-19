

# flatMap

Returns a single list of all elements yielded from results of transform function being invoked on each element of original array.

```kotlin
inline fun <T, R> Array<out T>.flatMap(transform: (T) -> Iterable<R>): List<R>(source)
```

```kotlin
val words = arrayOf("kotlin", "is", "fun")
val letters = words.flatMap { it.toList() }
println(letters)  // [k, o, t, l, i, n, i, s, f, u, n]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/flat-map.html)

    