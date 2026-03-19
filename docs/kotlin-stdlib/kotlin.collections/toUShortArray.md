

# toUShortArray

Returns an array of UShort containing all of the elements of this generic array.

```kotlin
@ExperimentalUnsignedTypesfun Array<out UShort>.toUShortArray(): UShortArray(source)
```

```kotlin
import kotlin.experimental.ExperimentalUnsignedTypes

@ExperimentalUnsignedTypes
fun main() {
    val array: Array<UShort> = arrayOf(1u, 2u, 3u, 65535u)
    val ushortArray: UShortArray = array.toUShortArray()
    println(ushortArray.joinToString(", ")) // prints: 1, 2, 3, 65535
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-u-short-array.html)

    