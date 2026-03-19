

# arrayOfNulls

Returns an array of objects of the given type with the given size, initialized with null values.

```kotlin
expect fun <T> arrayOfNulls(size: Int): Array<T?>(source)
```

```kotlin
val numbers: Array<Int?> = arrayOfNulls(4)

numbers[0] = 10
numbers[2] = 30

println(numbers.contentToString()) // Output: [10, null, 30, null]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/array-of-nulls.html)

    