

# toULongArray

Returns an array of ULong containing all of the elements of this generic array.

```kotlin
@ExperimentalUnsignedTypesfun Array<out ULong>.toULongArray(): ULongArray(source)
```

```kotlin
@ExperimentalUnsignedTypes
fun main() {
    // Create an Array of ULong values
    val uLongList: Array<ULong> = arrayOf(1uL, 2uL, 3uL, 4uL)

    // Convert the Array<ULong> to a ULongArray
    val uLongArray: ULongArray = uLongList.toULongArray()

    // Print the resulting ULongArray
    println(uLongArray.joinToString(prefix = "[", postfix = "]"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-u-long-array.html)

    