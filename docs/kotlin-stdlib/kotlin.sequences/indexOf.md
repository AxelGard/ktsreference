

# indexOf

Returns first index of element, or -1 if the sequence does not contain element.

```kotlin
fun <T> Sequence<T>.indexOf(element: T): Int(source)
```

```kotlin
val fruits = sequenceOf("apple", "banana", "cherry", "banana")

// Find first occurrence of "banana"
println(fruits.indexOf("banana"))   // prints 1

// Find an element that isn't present
println(fruits.indexOf("orange"))   // prints -1
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/index-of.html)

    