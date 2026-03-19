

# reduceRightOrNull

Accumulates value starting with the last element and applying operation from right to left to each element and current accumulator value.

```kotlin
inline fun <S, T : S> Array<out T>.reduceRightOrNull(operation: (T, acc: S) -> S): S?(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4)
val sum = numbers.reduceRightOrNull { current, acc -> current + acc }   // sum == 10

val words = arrayOf("kotlin", "is", "fun")
val sentence = words.reduceRightOrNull { word, acc -> word + " " + acc }   // sentence == "kotlin is fun"

val empty = arrayOf<Int>()
val result = empty.reduceRightOrNull { a, acc -> a + acc }   // result == null
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reduce-right-or-null.html)

    