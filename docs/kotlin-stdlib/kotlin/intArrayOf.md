

# intArrayOf

Returns an array containing the specified Int numbers.

```kotlin
expect fun intArrayOf(vararg elements: Int): IntArray(source)
```

```kotlin
val numbers = intArrayOf(1, 2, 3, 4, 5)
println(numbers.joinToString(prefix = "[", postfix = "]")) // [1, 2, 3, 4, 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/int-array-of.html)

    