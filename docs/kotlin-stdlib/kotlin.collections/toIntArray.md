

# toIntArray

Returns an array of Int containing all of the elements of this generic array.

```kotlin
fun Array<out Int>.toIntArray(): IntArray(source)
```

```kotlin
val numbers = arrayOf(10, 20, 30)
val intArray: IntArray = numbers.toIntArray()

println(intArray.joinToString())
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-int-array.html)

    