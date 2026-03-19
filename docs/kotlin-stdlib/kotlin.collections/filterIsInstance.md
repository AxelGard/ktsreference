

# filterIsInstance

Returns a list containing all elements that are instances of specified type parameter R.

```kotlin
inline fun <R> Array<*>.filterIsInstance(): List<R>(source)
```

```kotlin
val mixedArray: Array<Any> = arrayOf("hello", 42, "world", 3.14, 99)

val strings: List<String> = mixedArray.filterIsInstance<String>()
val ints: List<Int> = mixedArray.filterIsInstance<Int>()

println(strings) // [hello, world]
println(ints)    // [42, 99]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-is-instance.html)

    