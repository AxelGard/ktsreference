

# toTypedArray

Returns a typed object array containing all of the elements of this primitive array.

```kotlin
@ExperimentalUnsignedTypesfun UIntArray.toTypedArray(): Array<UInt>(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val uintArray: UIntArray = uintArrayOf(1u, 2u, 3u, 4u)
    val typedArray: Array<UInt> = uintArray.toTypedArray()
    println(typedArray.joinToString(prefix = "[", postfix = "]"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-typed-array.html)

    