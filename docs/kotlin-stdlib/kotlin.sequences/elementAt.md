

# elementAt

Returns an element at the given index or throws an IndexOutOfBoundsException if the index is out of bounds of this sequence.

```kotlin
fun <T> Sequence<T>.elementAt(index: Int): T(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(10, 20, 30, 40, 50)
    val value = numbers.elementAt(3) // element at index 3
    println("Element at index 3: $value") // prints 40
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/element-at.html)

    