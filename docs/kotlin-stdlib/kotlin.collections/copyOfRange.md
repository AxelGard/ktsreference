

# copyOfRange

Returns a new array which is a copy of the specified range of the original array.

```kotlin
@ExperimentalUnsignedTypesinline fun UIntArray.copyOfRange(fromIndex: Int, toIndex: Int): UIntArray(source)
```

```kotlin
@file:ExperimentalUnsignedTypes

fun main() {
    val original = uintArrayOf(10u, 20u, 30u, 40u, 50u)
    val subArray = original.copyOfRange(1, 4)   // copies elements at indices 1, 2, 3
    println(subArray.joinToString())           // prints: 20, 30, 40
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/copy-of-range.html)

    