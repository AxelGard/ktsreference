

# elementAtOrElse

Returns an element at the given index or the result of calling the defaultValue function if the index is out of bounds of this sequence.

```kotlin
fun <T> Sequence<T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T(source)
```

```kotlin
fun main() {
    // Create a sequence of the first 5 natural numbers
    val numbers = generateSequence(1) { it + 1 }.take(5) // 1, 2, 3, 4, 5

    // Get the element at index 2 (third element) – this exists
    val elementAtIndex2 = numbers.elementAtOrElse(2) { -1 }

    // Get the element at index 10 – this is out of bounds, so the default is used
    val elementAtIndex10 = numbers.elementAtOrElse(10) { -1 }

    println("Element at index 2: $elementAtIndex2")   // prints 3
    println("Element at index 10: $elementAtIndex10") // prints -1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/element-at-or-else.html)

    