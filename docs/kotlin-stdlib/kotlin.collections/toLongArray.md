

# toLongArray

Returns an array of Long containing all of the elements of this generic array.

```kotlin
fun Array<out Long>.toLongArray(): LongArray(source)
```

```kotlin
val boxedArray: Array<Long> = arrayOf(1L, 2L, 3L)
val longArray: LongArray = boxedArray.toLongArray()
println(longArray.contentToString())  // prints: [1, 2, 3]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-long-array.html)

    